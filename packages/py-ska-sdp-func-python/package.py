from spack.package import PythonPackage, depends_on, version


class PySkaSdpFuncPython(PythonPackage):
    """
    This repository contains Processing Function wrappers
    implemented in Python. The original code was migrated from RASCIL.
    """

    homepage = "https://gitlab.com/ska-telescope/sdp/ska-sdp-func-python"
    git = "https://gitlab.com/ska-telescope/sdp/ska-sdp-func-python"

    license("BSD-3-Clause", checked_by="scpmw")

    version("0.5.1", commit="46e78257e4684ed8f339e351c699d627debde6b0")
    version("develop", branch="main")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-poetry-core", type=("build", "run"))
    depends_on("py-astropy@6.1:", type=("build", "run"))
    depends_on("py-astroplan@0.10:", type=("build", "run"))
    depends_on("py-ducc@0.35:", type=("build", "run"))
    depends_on("py-numpy@1.26:", type=("build", "run"))
    # Newest version in spack, seems okay according to unit tests
    depends_on("py-photutils@1.5:", type=("build", "run"))
    depends_on("py-scipy@1.14:", type=("build", "run"))
    depends_on("py-xarray@2024.7:", type=("build", "run"))
    depends_on("py-reproject@0.14:", type=("build", "run"))
    depends_on("py-ska-sdp-datamodels@0.3.3:", type=("build", "run"))
    depends_on("py-ska-sdp-func", type=("build", "run"))
    depends_on("dp3+python@6.1:", type=("build", "run"))

    # Not needed yet...
    # depends_on("py-xradio@0.0.40", type=("build", "run"))
