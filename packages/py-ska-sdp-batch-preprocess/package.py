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

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-pyyaml@6.0.1:", type=("build", "run"))
    depends_on("py-jsonschema@4.4.0:", type=("build", "run"))
    depends_on("py-h5py@3.7.0:", type=("build", "run"))
    depends_on("dp3@6.0:", type=("build", "run"))
