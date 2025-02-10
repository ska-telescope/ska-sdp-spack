import os

import llnl.util.lang

from spack.package import PythonPackage


class PyDucc(PythonPackage):
    """Python bindings for Distinctly Useful Code Collection (DUCC)."""

    homepage = "https://gitlab.mpcdf.mpg.de/mtr/ducc"
    url = "https://gitlab.mpcdf.mpg.de/mtr/ducc.git"
    git = "https://gitlab.mpcdf.mpg.de/mtr/ducc.git"

    maintainers("saliei")

    license("Affero General Public License v1.0")

    version("develop-0.35.0", branch="ducc0", preferred=True)
    version("develop-0.34.0", branch="ducc0")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake", type="build")

    depends_on("python@3.8.0:", type="build")
    depends_on("py-setuptools@40.6.0:", type="build")
    depends_on("py-pybind11", type="build")
    depends_on("py-numpy@1.17.0:", type="build")

    depends_on("ducc", type=("build", "link"))

    @property
    @llnl.util.lang.memoized
    def _output_version(self):
        spec_vers_str = str(self.spec.version.up_to(3))
        if "develop" in spec_vers_str:
            # Remove 'develop-' from the version in spack
            spec_vers_str = spec_vers_str.partition("-")[2]
        return spec_vers_str

    def setup_build_environment(self, env):
        cmake_args = []
        cmake_args.append("-DDUCC_USE_THREADS=True")
        env.set("CMAKE_ARGS", " ".join(cmake_args))
        # a hack to overcome setuptools bug in not correctly
        # recognizing correct C++ Intel compiler.
        if "%oneapi" in self.spec:
            env.set("CC", os.environ.get("CXX"))
