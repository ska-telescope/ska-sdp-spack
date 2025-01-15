from spack.package import PythonPackage, depends_on, version


class PySkaSdpDatamodels(PythonPackage):
    """
    This repository contains high-level data models implemented in Python.
    These models were originally developed in RASCIL.
    """

    homepage = "https://gitlab.com/ska-telescope/sdp/ska-sdp-datamodels"
    git = "https://gitlab.com/ska-telescope/sdp/ska-sdp-datamodels"

    license("BSD-3-Clause", checked_by="scpmw")

    version("develop", branch="main")
    version(
        "0.3.3",
        commit="8ca3e42c75ffe294b3d11b6a23819117711176fb",
        preferred=True,
    )

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-poetry-core", type="build")
    depends_on("py-astropy@6.1:", type=("build", "run"))
    depends_on("py-astroplan@0.10:", type=("build", "run"))
    depends_on("py-h5py@3.11:", type=("build", "run"))
    depends_on("py-pandas@2.2:", type=("build", "run"))
    depends_on("py-numpy@1.26:", type=("build", "run"))
    depends_on("py-xarray@2024.7:", type=("build", "run"))
    depends_on("py-msgpack@1.0:", type=("build", "run"))
    depends_on("py-msgpack-numpy@0.4:", type=("build", "run"))
    depends_on("py-ska-telmodel@1.19:", type=("build", "run"))
    depends_on("py-casacore@3.5:", type=("build", "run"))
