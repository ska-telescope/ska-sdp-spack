# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Aoflagger(CMakePackage):
    """RFI detector and quality analysis
    for astronomical radio observations."""

    homepage = "https://sourceforge.net/projects/aoflagger/"
    git      = "https://gitlab.com/aroffringa/aoflagger.git"
    version('3.1.0', commit='18b70b9836552d7a632c457ffd8822e57a3ebe7b', submodules=True)

    depends_on('casacore')
    depends_on('cfitsio')
    depends_on('fftw')
    depends_on('boost+python+numpy')
    depends_on('hdf5')
    depends_on('libxml2')
    depends_on('lapack')
    depends_on('lua')
