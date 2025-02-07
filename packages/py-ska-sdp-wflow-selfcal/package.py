from spack.package import PythonPackage


class PySkaSdpWflowSelfcal(PythonPackage):
    """
    SKA iterative self-calibration pipeline, which internally performs
    calibration using DP3 and imaging using WSClean.
    """

    homepage = (
        "https://gitlab.com/ska-telescope/sdp/"
        "science-pipeline-workflows/ska-sdp-wflow-selfcal"
    )
    url = homepage + "/-/archive/0.3.0/ska-sdp-wflow-selfcal-0.3.0.tar.bz2"
    git = homepage

    maintainers("mnijhuis-tos")

    license("BSD 3-Clause")

    version("latest", branch="main", no_cache=True, deprecated=True)
    version("main", branch="main", no_cache=True)
    version("0.3.0", tag="0.3.0")
    version("0.3.1", tag="0.3.1")

    # Basic Python dependencies.
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-poetry-core", type="build")

    # The latest main typically requires very recent DP3 and WSClean versions.
    depends_on("dp3@latest", type="run", when="@latest")
    depends_on("wsclean@latest", type="run", when="@latest")
    depends_on("dp3@master", type="run", when="@main")
    depends_on("wsclean@master", type="run", when="@main")

    # Releases use fixed versions of DP3 and WSClean.
    depends_on("dp3@6.3", type="run", when="@0.3.1")
    depends_on("dp3@6.2.1", type="run", when="@0.3.0")
    depends_on("wsclean@3.5.1", type="run", when="@0.3.1")
    depends_on("wsclean@3.5", type="run", when="@0.3.0")

    # Other dependencies, which correspond to the project's pyproject.toml.
    depends_on("py-astropy@5.2.2:", type="run")
    depends_on("py-losoto@2.4.2:", type="run")
    depends_on("py-lsmtool@1.6.2:", type="run")
    depends_on("py-h5py@3.8.0:", type="run")
    depends_on("py-shapely@2.0.1:", type="run")
    depends_on("py-bdsf@1.10.2:", type="run")
    depends_on("py-requests@2.28.2:", type="run")
    depends_on("py-casacore@3.5.2:", type="run")
    depends_on("py-dask@2023.7.1:+distributed", type="run")
    depends_on("py-jsonschema@4.22.0:", type="run")
    depends_on("py-numpy@1.25:", type="run")
    depends_on("everybeam@0.6.1:", type="run")
