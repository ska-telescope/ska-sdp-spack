# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Everybeam(CMakePackage):
    """The EveryBeam library is a library that provides the antenna response
        pattern for several instruments, such as LOFAR (and LOBES), SKA (OSKAR),
        MWA, JVLA, etc."""

    homepage = "https://git.astron.nl/RD/EveryBeam"
    git      = "https://git.astron.nl/RD/EveryBeam.git"

    version('0.1.1', commit='v0.1.1', submodules=True)
    version('0.1.2', commit='v0.1.2', submodules=True)
    version('0.1.3', commit='v0.1.3', submodules=True)
    version('0.2.0', commit='v0.2.0', submodules=True)
    version('0.3.0', commit='v0.3.0', submodules=True)
    version('0.3.1', commit='v0.3.1', submodules=True)
    version('0.4.0', commit='v0.4.0', submodules=True)
    version('0.5.1', commit='v0.5.1', submodules=True)
    version('0.5.2', commit='v0.5.2', submodules=True)
    version('0.5.3', commit='v0.5.3', submodules=True)
    version('latest', branch='master', submodules=True)

    variant('debug-information', default=False, description='Enable debug information')
    variant('python', default=True, description='Enable Python support')

    depends_on('hdf5+cxx')
    depends_on('casacore+data')
    depends_on('boost+filesystem+system')
    depends_on('fftw')
    depends_on('gsl', when='@0.4.0:')
    depends_on('python', when='+python')
    depends_on('cmake@3.18.6', when='@0.2.0')
    depends_on('git')

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define('BUILD_WITH_PYTHON', '+python' in spec),
        ]
        if '+debug-information' in spec:
            args.append(self.define('CMAKE_CXX_FLAGS', "-g"))
        return args

    def setup_run_environment(self, env):
        spec = self.spec
        if ('+python') in spec:
            import re
            python_version = re.search(r'python@=([\d]+.[\d]+)', str(self.spec)).group(1)
            env.prepend_path('PYTHONPATH', join_path(self.prefix.lib, "python{}".format(python_version), 'site-packages'))
