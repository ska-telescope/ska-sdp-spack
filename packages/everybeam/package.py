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

    version('0.1.1', commit='21a36d40edc479a9bb0dacb06760fc2a5888953b', submodules=True)
    version('0.1.2', commit='f633da915ada8f67dd566bee2f7cc643ff2b9960', submodules=True)
    version('0.1.3', commit='0e1339782fa09d91f0cf37c3cf5f4a1aab62cd97', submodules=True)
    version('0.2.0', commit='74fe444e0052d1179126ba4742eec8392336019d', submodules=True)
    version('0.2.1', commit='c80fbffc3ba49ce0cc9a5d7ea38e2717b5b60d80', submodules=True) # Not an official release
    version('0.2.2', commit='37b37d33017b21bde0dec9d8ca05594b65ee7695', submodules=True) # Not an official release
    version('0.2.3', commit='4d6b8eac69ba26726fb50cff086c6d8d794283ce', submodules=True) # Not an official release
    version('0.3.0', commit='2eea95e1d93832d73b623be85085f18875a14fa5', submodules=True)
    version('latest', branch='master', submodules=True)

    variant('python', default=True, description='Enable Python support')

    depends_on('hdf5+cxx')
    depends_on('casacore')
    depends_on('boost+filesystem+system')
    depends_on('fftw')
    depends_on('python', when='+python')
    depends_on('cmake@3.18.6', when='@0.2.0')

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define('BUILD_WITH_PYTHON', '+python' in spec),
        ]
        return args

    def setup_run_environment(self, env):
        spec = self.spec
        if ('+python') in spec:
            import re
            python_version = re.search(r'python@([\d].[\d])', str(self.spec)).group(1)
            env.prepend_path('PYTHONPATH', join_path(self.prefix.lib, "python{}".format(python_version), 'site-packages'))
