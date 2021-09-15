# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Idg(CMakePackage):
    """Image Domain Gridding (IDG) is a fast method for convolutional
       resampling (gridding/degridding) of radio astronomical data (visibilities).
       Direction dependent effects (DDEs) or A-tems can be applied in the gridding
       process."""

    homepage = "https://www.astron.nl/citt/IDG/"
    git      = "https://git.astron.nl/RD/idg"

    version('master', commit='f3dce7b1b395d9d37a484fb7cf05079147f34b2d')

    depends_on('fftw')
    depends_on('openblas')
    depends_on('cuda')
    depends_on('python')

    def cmake_args(self):
        args = [
            self.define('BUILD_LIB_CPU', True),
            self.define('BUILD_LIB_CUDA', True),
            self.define('BUILD_WITH_PYTHON', True),
            self.define('PERFORMANCE_REPORT', True),
        ]

        return args

    def setup_run_environment(self, env):
        env.prepend_path('PATH', join_path(self.prefix.bin, 'examples', 'cxx'))
        env.prepend_path('PATH', join_path(self.prefix.bin, 'examples', 'python'))
