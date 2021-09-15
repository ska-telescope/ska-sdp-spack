# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Dp3(CMakePackage):
    """LOFAR preprocessing software, including averaging,
	flagging, various kinds of calibration and more."""

    homepage = "https://www.astron.nl/citt/DP3"
    git      = "https://git.astron.nl/RD/DP3.git"

    version('5.1', commit='f2a8afd677f2bff3937bb1c350d1b0ad340bb514', submodules=True)

    depends_on('aoflagger@3.1.0')
    depends_on('everybeam@0.1.3')
