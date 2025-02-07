from spack.package import *


class Dysco(CMakePackage):
    """A compressing storage manager for Casacore mearement sets."""

    homepage = "https://github.com/aroffringa/dysco/wiki"
    git      = "https://github.com/aroffringa/dysco.git"

    version('1.2', commit='v1.2', submodules=True)
    version('latest', branch='master', submodules=True, no_cache=True, deprecated=True)
    version('master', branch='master', submodules=True, no_cache=True)

    depends_on('boost+date_time+program_options')
    depends_on('casacore')
    depends_on('git')
    depends_on('gsl')
    depends_on('openblas threads=pthreads')
    depends_on('python')

    def setup_build_environment(self, env):
        env.set("OPENBLAS_NUM_THREADS", "1")

    def setup_run_environment(self, env):
        env.set("OPENBLAS_NUM_THREADS", "1")
        env.prepend_path("LD_LIBRARY_PATH", join_path(self.prefix, "lib"))
