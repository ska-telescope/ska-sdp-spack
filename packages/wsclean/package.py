# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Wsclean(CMakePackage):
    """WSClean (w-stacking clean) is a fast generic widefield imager. It
       implements several gridding algorithms and offers fully-automated multi-scale
       multi-frequency deconvolution."""

    homepage = "https://wsclean.readthedocs.io/"
    git      = "https://gitlab.com/aroffringa/wsclean.git"

    version('3.0', commit='9ee587c576caad779dc127bb3f83858513679333', submodules=True)

    depends_on('hdf5-autotools+cxx')
    depends_on('fftw')
    depends_on('casacore@3.3.0')
    depends_on('everybeam')
    depends_on('cuda')
    depends_on('idg')
    depends_on('boost')
