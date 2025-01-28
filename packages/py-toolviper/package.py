from spack.package import PythonPackage, depends_on, version


class PyToolviper(PythonPackage):
    """
    Tools and utilities for otimized radio astronomy processing
    using the VIPER framework.
    """

    homepage = "https://github.com/casangi/toolviper"
    git = "https://github.com/casangi/toolviper.git"

    license("BSD-3-Clause", checked_by="scpmw")

    version("0.0.2", commit="v0.0.2")
    version("develop", branch="main")

    # These dependencies are likely incorrect and/or not enough
    # to use all functions required by e.g. graphviper. We are basically
    # only maintaining this for supporting testing of xarray.

    depends_on("py-cerberus", type=("build", "run"))
    depends_on("py-dask", type=("build", "run"))
    # Doesn't exist in Spack yet, not actually needed for our purposes?
    # depends_on('py-dask-jobqueue',type=("build", "run"))
    depends_on("py-distributed", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-ipywidgets", type=("build", "run"))
    depends_on("py-rich", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-zarr", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
