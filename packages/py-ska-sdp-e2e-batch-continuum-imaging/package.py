from spack.package import (  # pylint: disable=redefined-builtin
    PythonPackage,
    depends_on,
    license,
    maintainers,
    version,
)


class PySkaSdpE2eBatchContinuumImaging(PythonPackage):
    """SKA SDP End-to-End Batch Continuum Imaging."""

    homepage = (
        "https://gitlab.com/ska-telescope/sdp/science-pipeline-workflows/"
        + "ska-sdp-e2e-batch-continuum-imaging"
    )
    git = homepage

    maintainers("nimalan", "justin")

    license("BSD 3-Clause")

    version("0.1.0", tag="0.1.0")
    version("main", branch="main")

    depends_on("python@3.10", type=("build", "run"))
    depends_on("py-poetry-core", type="build")
    depends_on("py-yaml@6.0.2:", type="run")
    depends_on("py-dask@2023.7.1:+distributed", type="run")
    depends_on("py-typer@0.12.5:", type="run")
