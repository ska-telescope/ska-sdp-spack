from spack.package import PythonPackage


class PySkaSdpE2eBatchContinuumImaging(PythonPackage):
    """SKA SDP End-to-End Batch Continuum Imaging."""

    homepage = (
        "https://gitlab.com/ska-telescope/sdp/science-pipeline-workflows/"
        + "ska-sdp-e2e-batch-continuum-imaging"
    )
    git = homepage

    maintainers("nimalan-m", "t3pleni9")

    license("BSD 3-Clause")

    version("0.1.0", tag="0.1.0")
    version("0.2.0", tag="0.2.0")
    version("main", branch="main")

    depends_on("python@3.10", type=("build", "run"))
    depends_on("py-poetry-core", type="build")
    depends_on("py-yaml@6.0.2:", type="run")
    depends_on("py-dask@2023.7.1:+distributed", type="run")
    depends_on("py-typer", type="run")
