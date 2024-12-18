
from spack.package import *

class PyAstroplan(PythonPackage):
    """
    astroplan is an open source Python package to help astronomers
    plan observations.

    The goal of astroplan is to make a flexible toolbox for
    observation planning and scheduling. When complete, the goal is to
    be easy for Python beginners and new observers to to pick up, but
    powerful enough for observatories preparing nightly and long-term
    schedules.
    """
    
    homepage = "https://github.com/astropy/astroplan.git"
    pypi = "astroplan/astroplan-0.10.1.tar.gz"

    license("BSD-3-Clause", checked_by="scpmw")

    version('0.10.1', sha256="39d97c3377e1630abff3a94d8c956980f77a3e809e27a0376dd7d30abe3b6959")

    depends_on("py-numpy@1.17:", type=("build", "run"))
    depends_on("py-astropy@6:", type=("build", "run"))
    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build")
    depends_on("py-pytz", type=("build", "run"))
    depends_on("py-six", type=("build", "run")) # Fails without it

