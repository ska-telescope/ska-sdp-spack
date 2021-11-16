# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Lofarstman(CMakePackage):
    """Lofar storage manager."""

    homepage = "https://github.com/lofar-astron/LofarStMan"
    git      = "https://github.com/lofar-astron/LofarStMan.git"

    version('latest', branch='master')

    depends_on('casacore@3.3.0')
