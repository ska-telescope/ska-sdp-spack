from spack.package import CMakePackage, depends_on, variant, version


class Wsclean(CMakePackage):
    """WSClean (w-stacking clean) is a fast generic widefield imager. It
    implements several gridding algorithms and offers fully-automated
    multi-scale multi-frequency deconvolution."""

    homepage = "https://wsclean.readthedocs.io/"
    git = "https://gitlab.com/aroffringa/wsclean.git"

    version("3.0", commit="v3.0", submodules=True)
    version("3.0.1", commit="v3.0.1", submodules=True)
    version("3.1", commit="v3.1", submodules=True)
    version("3.2", commit="v3.2", submodules=True)
    version("3.3", commit="v3.3", submodules=True)
    version("3.4", commit="v3.4", submodules=True)
    version("3.5", commit="v3.5", submodules=True)
    version(  # master branch at 2025-01-27
        "3.5.1",
        commit="d7d89fddf472ffac05a2fa1820ec7d0027da38ee",
        submodules=True,
        preferred=True,
    )
    version(
        "latest", branch="master", submodules=True, no_cache=True, deprecated=True
    )
    version(
        "master",
        branch="master",
        submodules=True,
        no_cache=True,
    )

    variant("python", default=False, description="Enable Python support")
    variant("cuda", default=False, description="Enable CUDA support")

    depends_on("hdf5+cxx+threadsafe")
    depends_on("fftw")
    depends_on("casacore+data")
    depends_on("everybeam@0.2.0", when="@3.0")
    depends_on("everybeam@0.3.0", when="@3.0.1")
    depends_on("everybeam@0.3.0", when="@3.1")
    depends_on("everybeam@0.4.0", when="@3.2")
    depends_on("everybeam@0.5.1", when="@3.3")
    depends_on("everybeam@0.5.3", when="@3.4")
    depends_on("everybeam@0.6:0.7", when="@3.5")
    depends_on("everybeam@0.6:0.7", when="@3.6:")
    depends_on("everybeam@0.6:0.7", when="@latest")
    depends_on("dp3@6.1:,latest", when="@latest")
    depends_on("dp3@6.1:", when="@master")
    depends_on("idg@1.0.0", when="@3.1")
    depends_on("idg@1.1.0", when="@3.2")
    depends_on("idg@1.1.0", when="@3.3")
    depends_on("idg@1.2.0", when="@3.4:")
    depends_on("idg@latest", when="@latest")
    depends_on("idg@master", when="@master")
    depends_on("idg+cuda", when="+cuda")
    depends_on("idg+python", when="+python")
    depends_on("boost+date_time+program_options")
    depends_on("openblas threads=pthreads")
    depends_on("gsl")
    depends_on("git")
    depends_on("python")

    def setup_build_environment(self, env):
        env.set("OPENBLAS_NUM_THREADS", "1")

    def setup_run_environment(self, env):
        env.set("OPENBLAS_NUM_THREADS", "1")
