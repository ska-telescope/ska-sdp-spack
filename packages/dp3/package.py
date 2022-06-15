# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Dp3(CMakePackage):
    """LOFAR preprocessing software, including averaging,
	flagging, various kinds of calibration and more."""

    homepage = "https://dp3.readthedocs.io"
    git      = "https://git.astron.nl/RD/DP3.git"

    version('5.0', commit='50de337bed30525a4c0583ea977a58c976a7cc39', submodules=True)
    version('5.1', commit='f2a8afd677f2bff3937bb1c350d1b0ad340bb514', submodules=True)
    version('5.2', commit='b2e0f5e2dfb88312540bd99258e84e761c08e7ea', submodules=True)
    version('latest', branch='master', submodules=True)

    variant('python', default=True, description='Enable Python support')

    depends_on('aoflagger@3.1.0')
    depends_on('everybeam@0.3.0', when='@5.2')
    depends_on('everybeam@0.1.3', when='@5.1')
    depends_on('everybeam@0.1.1', when='@5.0')
    depends_on('everybeam@latest', when='@latest')
    depends_on('openblas', when='@5.2')
    depends_on('openblas', when='@latest')
    depends_on('boost')
    depends_on('hdf5')

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
            python_version = re.search(r'python@([\d].[\d])', str(self.spec)).group(1)
            env.prepend_path('PYTHONPATH', join_path(self.prefix.lib, "python{}".format(python_version), 'site-packages'))
