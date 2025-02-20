from spack.package import PythonPackage


class PyRapidsBuildBackend(PythonPackage):
    """
    rapids-build-backend is an adapter around PEP517 builders that provides
    support for key RAPIDS requirements. The package's primary purpose is
    to automate the various bits of preprocessing that are typically
    done to RAPIDS package metadata prior to publishing packages.
    """

    homepage = "https://github.com/rapidsai/rapids-build-backend"
    git = "https://github.com/rapidsai/rapids-build-backend"
    url = "https://github.com/rapidsai/\
    rapids-build-backend/archive/refs/tags/v0.3.2.tar.gz"

    maintainers("saliei")

    license("Apache-2.0-License")

    version("main", branch="main")
    version(
        "0.3.2",
        sha256="11ed069adf2b6b70b8f45e5d8e3947ed8f669e4cd7e7245f491b86f0c1f0a01d",
        preferred=True,
    )
    version(
        "0.3.1",
        sha256="0d97ab05dc7bb6180b8788d29ca4d4855119792f31217c8d71af23b83792dfeb",
    )
    version(
        "0.3.0",
        sha256="98f58ece94040b8678cb2a00ef5a8cfdced00fd3fdc0fa41ed45ffe04d84981d",
    )

    depends_on("python", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")
