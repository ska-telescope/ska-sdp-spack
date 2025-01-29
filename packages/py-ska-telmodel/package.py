from spack.package import PythonPackage, depends_on, version


class PySkaTelmodel(PythonPackage):
    """
    Library for retrieving and working with SKA Telescope Model information.
    """

    homepage = "https://gitlab.com/ska-telescope/ska-telmodel"
    git = "https://gitlab.com/ska-telescope/ska-telmodel"

    license("BSD-3-Clause", checked_by="scpmw")

    version("1.19.7", commit="9537d36c7cdd23f41cd23ddf5bab3b4f89a92c3a")
    version("develop", branch="master")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-poetry-core", type=("build", "run"))
    depends_on("py-schema@0.7.5:", type=("build", "run"))
    depends_on("py-appdirs@1.4.4:", type=("build", "run"))
    depends_on("py-toolz@0.12.0:", type=("build", "run"))
    depends_on("py-pyyaml@6.0:", type=("build", "run"))
    # 7.3 is enough it seems (checked unit tests)
    depends_on("py-overrides@7.3:", type=("build", "run"))
    depends_on("py-gitpython@3.1:", type=("build", "run"))
    depends_on("py-python-gitlab@3.8:", type=("build", "run"))
    depends_on("py-tomli@2.0:", type=("build", "run"))
    depends_on("py-filelock@3.12:", type=("build", "run"))
    depends_on("py-prettytable@3.7:", type=("build", "run"))
    # Required for ska_telmodel.data (according to unit tests)
    depends_on("py-requests@2.32:", type=("build", "run"))
    # Currently only for tests, but will shortly become a run dependency
    depends_on("py-jsonschema@4.0:", type=("build", "run"))
