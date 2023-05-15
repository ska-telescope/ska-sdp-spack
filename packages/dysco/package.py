# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Dysco(CMakePackage):
    """A compressing storage manager for Casacore mearement sets."""

    homepage = "https://github.com/aroffringa/dysco/wiki"
    git      = "https://github.com/aroffringa/dysco.git"

    version('1.2', commit='425895c97806125995e74de11d075c8760022fd6', submodules=True)
    version('latest', branch='master', submodules=True, preferred=True)

    depends_on('casacore')
    depends_on('boost+date_time+program_options')
    depends_on('openblas threads=pthreads')
    depends_on('gsl')
    depends_on('git')
    depends_on('python')

    def setup_build_environment(self, env):
        env.set("OPENBLAS_NUM_THREADS", "1")

    def setup_run_environment(self, env):
        env.set("OPENBLAS_NUM_THREADS", "1")
        spec = self.spec
