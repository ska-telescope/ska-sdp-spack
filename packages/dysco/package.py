# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Dysco(CMakePackage):
    """A compressing storage manager for Casacore mearement sets."""

    homepage = "https://github.com/aroffringa/dysco/wiki"
    git      = "https://github.com/aroffringa/dysco.git"

    version('1.2', commit='v1.2', submodules=True)
    version('latest', branch='master', submodules=True, preferred=True)

    depends_on('boost+date_time+program_options')
    depends_on('casacore')
    variant('debug-information', default=False, description='Enable debug information')
    depends_on('git')
    depends_on('gsl')
    depends_on('openblas threads=pthreads')
    depends_on('python')

    def cmake_args(self):
        spec = self.spec
        args = []
        if '+debug-information' in spec:
            args = [
                self.define('CMAKE_CXX_FLAGS', "-g")
            ]
        return args

    def setup_build_environment(self, env):
        env.set("OPENBLAS_NUM_THREADS", "1")

    def setup_run_environment(self, env):
        env.set("OPENBLAS_NUM_THREADS", "1")
        env.prepend_path("LD_LIBRARY_PATH", join_path(self.prefix, "lib"))
        spec = self.spec
