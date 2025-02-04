from spack.package import PythonPackage


class PyDaskCuda(PythonPackage):
    """
    Various utilities to improve deployment and management of
    Dask workers on CUDA-enabled systems. This library is experimental,
    and its API is subject to change at any time without notice.
    Dask-CUDA is a library extending Dask.distributed's single-machine
    LocalCluster and Worker for use in distributed GPU workloads.
    It is a part of the RAPIDS suite of open-source software libraries
    for GPU-accelerated data science.
    """

    homepage = "https://docs.rapids.ai/api/dask-cuda/stable/"
    git = "https://github.com/rapidsai/dask-cuda"
    url = "https://github.com/rapidsai/dask-cuda/archive/refs/tags/v24.12.00.tar.gz"

    maintainers("saliei")

    license("Apache-2.0-License")

    version("develop-25.04", branch="branch-25.04")
    version("24.12.00", sha256="0e72ee7b0b894fea70b6f39944ffb0f0cdcb6db78d6a891774e14f4965db8d10", preferred=True)
    version("24.10.00", sha256="7e3f8ece55023005b1d09f6a73cdea4aa802f5b62adfd5480423808087a20841")
    version("24.08.00", sha256="ab65debe72e8ed8d3df573a3e849672104556e9b144ff910820a0cea09cb3fc8")
    version("24.06.00", sha256="8f46f34deb2c0d692d9d1aefbdbd7a7c5daaee35b330322ac3c202c8102fc66b")
    version("24.04.00", sha256="5a3493c60cef5796d615473acaca416d9a6c685b85c1b601262b34c9431b36eb")
    version("24.02.00", sha256="6cdfe600c6cdd2a3fb82d6a58dd2acfed2c82f4b32b2ab5611d2cc9292fd2f2a")

    depends_on("python", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-rapids-build-backend", type="build")
    depends_on("py-rapids-dependency-file-generator", type="build")

    depends_on("py-dask", type=("build", "run"))
    depends_on("py-click", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pynvml", type=("build", "run"))
    depends_on("py-zict", type=("build", "run"))

    @property
    @llnl.util.lang.memoized
    def _output_version(self):
        spec_vers_str = str(self.spec.version.up_to(3))
        if "develop" in spec_vers_str:
            # Remove 'develop-' from the version in spack
            spec_vers_str = spec_vers_str.partition("-")[2]
        return spec_vers_str
