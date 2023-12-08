# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Dp3(CMakePackage):
    """LOFAR preprocessing software, including averaging,
	flagging, various kinds of calibration and more."""

    homepage = "https://dp3.readthedocs.io"
    git      = "https://git.astron.nl/RD/DP3.git"

    version('5.0', commit='v5.0', submodules=True)
    version('5.1', commit='v5.1', submodules=True)
    version('5.2', commit='v5.2', submodules=True)
    version('5.3', commit='v5.3', submodules=True)
    version('6.0', commit='v6.0', submodules=True)
    version('latest', branch='master', submodules=True)

    variant('python', default=True, description='Enable Python support')

    depends_on('aoflagger@3.4.0', when='@latest')
    depends_on('aoflagger@3.4.0', when='@6.0:')
    depends_on('aoflagger@3.2.0', when='@5.3')
    depends_on('aoflagger@3.1.0', when='@:5.2')
    depends_on('everybeam@0.5.3', when='@latest')
    depends_on('everybeam@0.5.3', when='@6.0:')
    depends_on('everybeam@0.3.0', when='@5.3')
    depends_on('everybeam@0.3.0', when='@5.2')
    depends_on('everybeam@0.1.3', when='@5.1')
    depends_on('everybeam@0.1.1', when='@5.0')
    depends_on('openblas threads=pthreads')
    depends_on('boost+date_time+test+program_options')
    depends_on('hdf5')
    depends_on('gsl')
    depends_on('git')
    variant('debug-information', default=False, description='Enable debug information')

    def cmake_args(self):
        spec = self.spec
        args = []
        if '+debug-information' in spec:
            args = [
                self.define('CMAKE_CXX_FLAGS', "-g")
            ]
        return args

    def setup_build_environment(self, env):
        print(self.spec.version)
        if (self.spec.satisfies('@latest') or
           int(str(self.spec.version.joined)) >= 52):
            env.set("OPENBLAS_NUM_THREADS", "1")

    def setup_run_environment(self, env):
        env.set("OPENBLAS_NUM_THREADS", "1")
        spec = self.spec
        if ('+python') in spec:
            import re
            python_version = re.search(r'python@=([\d.]+)', str(self.spec)).group(1)
            env.prepend_path('PYTHONPATH', join_path(self.prefix.lib, "python{}".format(python_version), 'site-packages'))
