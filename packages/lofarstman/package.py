from spack.package import *


class Lofarstman(CMakePackage):
    """Lofar storage manager."""

    homepage = "https://github.com/lofar-astron/LofarStMan"
    git      = "https://github.com/lofar-astron/LofarStMan.git"

    version('latest', branch='master')

    depends_on('casacore+data')
