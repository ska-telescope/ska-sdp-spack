from spack.package import PythonPackage, depends_on, maintainers, variant, version


class PyBdsf(PythonPackage):
    """Blob Detection and Source Finder"""

    homepage = "https://pybdsf.readthedocs.io"
    git = "https://github.com/lofar-astron/PyBDSF"
    pypi = "bdsf/bdsf-1.0.0.tar.gz"

    maintainers("mnijhuis-tos")
    license("GPLv3", checked_by="mnijhuis-tos")

    version(
        "1.12.0",
        sha256="1ec301d7f98dd9dcc51245a793b63fa6a341f6378fea45907e06c6a453b6940a",
    )

    variant(
        "rap",
        default=False,
        description="Support reading 'rap' images using CasaCore.",
    )

    depends_on("python@3.8:3.12", type="build")
    depends_on("py-setuptools@:64", type="build")
    depends_on("py-scikit-build@0.13:", type="build")
    depends_on("cmake@3.18:", type="build")
    depends_on("ninja", type="build")

    depends_on("boost+python+numpy", type=("build", "run"))
    depends_on("py-astropy", type="run")
    depends_on("py-scipy", type="run")
    depends_on("py-numpy@1", type="run")
    depends_on("py-matplotlib", type="run")

    depends_on("py-casacore", type="run", when="+rap")
