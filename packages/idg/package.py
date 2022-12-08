# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Idg(CMakePackage):
    """Image Domain Gridding (IDG) is a fast method for convolutional
       resampling (gridding/degridding) of radio astronomical data (visibilities).
       Direction dependent effects (DDEs) or A-tems can be applied in the gridding
       process."""

    homepage = "https://idg.readthedocs.io"
    git      = "https://git.astron.nl/RD/idg.git"

    version('0.8.1', commit='a09f3c85094c592f9304fff4c31e920c7592c3c3', submodules=True)
    version('latest', branch='master', preferred=True)

    variant('cuda', default=False, description='Enable CUDA support')
    variant('python', default=False, description='Enable Python support')
    variant('report', default=False, description='Enable performance reporting')

    depends_on('fftw')
    depends_on('openblas')
    depends_on('cuda', when='+cuda')
    depends_on('python', when='+python')

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define('BUILD_LIB_CPU', True),
            self.define('BUILD_LIB_CUDA', '+cuda' in spec),
            self.define('BUILD_WITH_PYTHON', '+python' in spec),
            self.define('PERFORMANCE_REPORT', '+report' in spec),
        ]
        return args

    def setup_run_environment(self, env):
        env.prepend_path('PATH', join_path(self.prefix.bin, 'examples', 'cxx'))
        spec = self.spec
        if ('+python') in spec:
            env.prepend_path('PATH', join_path(self.prefix.bin, 'examples', 'python'))
            import re
            python_version = re.search(r'python@([\d].[\d])', str(spec)).group(1)
            env.prepend_path('PYTHONPATH', join_path(self.prefix.lib, "python{}".format(python_version), 'site-packages'))
