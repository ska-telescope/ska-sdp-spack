from spack.package import *


class PyLosoto(PythonPackage):
    """LoSoTo: LOFAR solutions tool"""

    homepage = "http://github.com/revoltek/losoto/"
    pypi = "losoto/losoto-1.0.0.tar.gz"

    maintainers("mnijhuis-tos")

    license("GPLv3", checked_by="mnijhuis-tos")

    version(
        "2.4.4",
        sha256="94372a12b743b408353ae54ff4a6a479f790f9f7616aecf64db2eebbe87c0b89",
    )

    depends_on("python@3", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-tables@3.4.0:", type="run")
    depends_on("py-h5py@3.8.5:", type="run")
    depends_on("py-numpy@1.9.0:1", type="run")
    depends_on("py-scipy@1.4:", type="run")
    depends_on("py-matplotlib", type="run")
    depends_on("py-casacore@3.0:", type="run")
