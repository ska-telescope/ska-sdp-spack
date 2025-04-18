from spack.package import PythonPackage


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

    version("latest", branch="main", no_cache=True, deprecated=True)
    version("main", branch="main", no_cache=True)
    version("2.3.0", tag="2.3.0")
    version("2.2.0", tag="2.2.0")
    version("2.1.1", tag="2.1.1")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-poetry-core", type="build")
    depends_on("py-pyyaml@6.0.1:", type=("build", "run"))
    depends_on("py-jsonschema@4.4.0:", type=("build", "run"))
    depends_on("py-h5py@3.7.0:", type=("build", "run"))
    depends_on("py-dask@2024.7.1:", type=("build", "run"))
    depends_on("py-distributed@2024.7.1:", type=("build", "run"))
    depends_on("dp3@6.1:", type=("build", "run"))
