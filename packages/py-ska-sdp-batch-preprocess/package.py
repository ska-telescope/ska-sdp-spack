from spack.package import (  # pylint: disable=redefined-builtin
    PythonPackage,
    depends_on,
    license,
    maintainers,
    version,
)


class PySkaSdpBatchPreprocess(PythonPackage):
    """The Batch Preprocessing Pipeline prepares visibility data in MSv2 format
    before they can be sent off for self-calibration and imaging. The stages in
    typical order of run include: Static flagging, Dynamic flagging,
    Application of calibration solutions, and Averaging of the data."""

    homepage = (
        "https://gitlab.com/ska-telescope/sdp/"
        "science-pipeline-workflows/ska-sdp-batch-preprocess/"
    )
    url = (
        "https://gitlab.com/ska-telescope/sdp/"
        "science-pipeline-workflows/ska-sdp-batch-preprocess/-/"
        "archive/1.0.1/ska-sdp-batch-preprocess-1.0.1.tar.gz"
    )
    git = (
        "https://gitlab.com/ska-telescope/sdp/"
        "science-pipeline-workflows/ska-sdp-batch-preprocess/"
    )

    maintainers("saliei", "vmorello")

    license("BSD 3-Clause")

    version("latest", branch="main", preferred=True)
    version("2.2.0", commit="98747f8fa7064c770cd2b7b9e6232f0fdc722ea4")
    version("2.1.1", commit="0754ad2ca1fa67978ba30af8a38f03189e158c1f")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-poetry-core", type="build")
    depends_on("py-pyyaml@6.0.1:", type=("build", "run"))
    depends_on("py-jsonschema@4.4.0:", type=("build", "run"))
    depends_on("py-h5py@3.7.0:", type=("build", "run"))
    depends_on("dp3@6.0:", type=("build", "run"))
