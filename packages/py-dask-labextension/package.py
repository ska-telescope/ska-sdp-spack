from spack.package import PythonPackage

class PyDaskLabextension(PythonPackage):
    """
    This package provides a JupyterLab extension to manage Dask clusters, 
    as well as embed Dask's dashboard plots directly into JupyterLab panes.
    """

    homepage = "https://github.com/dask/dask-labextension"
    git = "https://github.com/dask/dask-labextension"
    url = "https://github.com/dask/dask-labextension/archive/refs/tags/7.0.0.tar.gz"

    maintainers("saliei")

    license("BSD-3-Clause")

    version("latest", branch="main")
    version("7.0.0", sha256="efd58cade518d8c95a94b2176f428b84a1acdeada575ac5389ee753c65c0a5bd")
    version("6.1.0", sha256="82d133a734071e0e75516c12de795a3a196a04148052922cb90e4a0b8e48e013")
    version("6.0.0", sha256="e56b21aea6ee01505f53ecbe26118d96e2e0fb7c98e5a60f6d2738342959ce66")

    depends_on("python", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-nodejs-version", type="build")
    depends_on("py-jupyterlab", type=("build", "run"))
    depends_on("py-bokeh", type=("build", "run"))
    depends_on("py-distributed", type=("build", "run"))
    depends_on("py-jupyter-server-proxy", type=("build", "run"))
