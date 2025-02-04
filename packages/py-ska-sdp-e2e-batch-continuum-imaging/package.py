from spack.package import (  # pylint: disable=redefined-builtin
    PythonPackage,
    depends_on,
    license,
    maintainers,
    version,
)


class PySkaSdpE2eBatchContinuumImaging(PythonPackage):
    """SKA SDP End-to-End Batch Continuum Imaging."""

    homepage = "https://gitlab.com/ska-telescope/sdp/science-pipeline-workflows/ska-sdp-e2e-batch-continuum-imaging"
    git = "https://gitlab.com/ska-telescope/sdp/science-pipeline-workflows/ska-sdp-e2e-batch-continuum-imaging"

    maintainers("nimalan", "justin")

    license("BSD-3-Clause", checked_by="scpmw")

    version("0.1.0", commit="618168aee1aea8e991063fd2cdd079cda03505ef")
    version("latest", branch="main")

    depends_on("python@3.10", type=("build", "run"))
