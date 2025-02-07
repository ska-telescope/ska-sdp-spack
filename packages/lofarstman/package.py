from spack.package import *


class Lofarstman(CMakePackage):
    """Lofar storage manager."""

    homepage = "https://github.com/lofar-astron/LofarStMan"
    git      = "https://github.com/lofar-astron/LofarStMan.git"

    version('latest', branch='master', no_cache=True, deprecated=True)
    version('master', branch='master', no_cache=True)

    depends_on('casacore+data')
