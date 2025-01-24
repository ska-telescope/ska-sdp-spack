from spack.package import PythonPackage, depends_on, maintainers, version


class PySkaSdpDistributedSelfCalPrototype(PythonPackage):
    """
    Prototype self-calibration pipeline to distribute processing
    across HPC cluster nodes, allowing scalability for large datasets
    and a reduction in overall computation time.
    """

    homepage = (
        "https://gitlab.com/ska-telescope/sdp/"
        "science-pipeline-workflows/ska-sdp-distributed-self-cal-prototype"
    )
    git = (
        "https://gitlab.com/ska-telescope/sdp/"
        "science-pipeline-workflows/ska-sdp-distributed-self-cal-prototype.git"
    )

    license("BSD-3-Clause", checked_by="sstansill")
    maintainers("milhazes", "sstansill", "max_m17", "mmacleod_za", "gemmadanks")

    version("0.1.0", commit="v0.1.0", submodules=True)
    version("0.2.0", commit="v0.2.0", submodules=True)
    version("latest", branch="main", submodules=True, preferred=True)

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-yaml@6.0.2:", type=("build", "run"))
    depends_on("py-zarr@2.16.1:", type=("build", "run"))
    depends_on("py-matplotlib@3.8.3:", type=("build", "run"))
    depends_on("py-xradio@0.0.41", type=("build", "run"))
    # Not Spack-ified yet!
    # depends_on('py-pylru@1.2.1:', type=("build", "run"))
    depends_on("py-numpy@1.25:", type=("build", "run"))
    depends_on("py-dask@2024.7:", type=("build", "run"))
    # 2024.7 is enough, to my knowledge not actually using any newer features
    depends_on("py-distributed@2024.7:", type=("build", "run"))
    depends_on("py-poetry-core", type="build")
    depends_on("py-xarray@2023.10.1:", type=("build", "run"))
    depends_on("py-astropy@6:", type=("build", "run"))
    depends_on("py-ska-sdp-exec-swiftly@1.0.0:", type=("build", "run"))
    depends_on("py-ska-sdp-func@1.2.0:", type=("build", "run"))
    depends_on("py-ska-sdp-func-python@0.5.1:", type=("build", "run"))
    depends_on("py-ska-sdp-datamodels@0.3.0:", type=("build", "run"))
