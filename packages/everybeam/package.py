# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Everybeam(CMakePackage):
    """The EveryBeam library is a library that provides the antenna response
        pattern for several instruments, such as LOFAR (and LOBES), SKA (OSKAR),
        MWA, JVLA, etc."""

    homepage = "https://git.astron.nl/RD/EveryBeam"
    git      = "https://git.astron.nl/RD/EveryBeam.git"

    version('0.1.3', commit='0e1339782fa09d91f0cf37c3cf5f4a1aab62cd97', submodules=True)
    version('0.2.0', commit='74fe444e0052d1179126ba4742eec8392336019d', submodules=True)

    depends_on('casacore@3.3.0', when='@0.1.3')
    depends_on('casacore@3.4.0', when='@0.2.0')
