from spack.package import PythonPackage, version, license, maintainers, depends_on


class PyLsmtool(PythonPackage):
    """LOFAR Sky model tool"""

    homepage = "https://lsmtool.readthedocs.io"
    git = "https://git.astron.nl/RD/LSMTool"
    pypi = "lsmtool/lsmtool-1.0.0.tar.gz"

    maintainers("mnijhuis-tos")
    license("GPLv3", checked_by="mnijhuis-tos")

    version("1.6.post1", sha256="84736672881107d1b607074d14a598b63509d5d66d1c9b4e436f9ae1a57c33a3")
    version("1.6", sha256="d06e2ae67fb31d136b5160d0847183061a8da1da6e12c9b7ba128d07810454f2")

    depends_on("python@3:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build")
    depends_on("py-scikit-build-core", type="build")
    depends_on("cmake@3.15:", type="build")
    depends_on("ninja@1.5:", type="build")

    depends_on("py-numpy@1", type="run")
    depends_on("py-scipy@0.11:", type="run")
    depends_on("py-matplotlib@0.99:", type="run")
    depends_on("py-astropy@3.2:", type="run")
    depends_on("everybeam@0.6.1:", type="run")
    depends_on("py-casacore", type="run")

    #lsmtool can optionally use pyvo, however, there's no pyvo spack package yet.
    #variant("vo", default=False, description="Enable Virtual Observatory access")
    #depends_on("py-pyvo", type="run", when="+vo")
