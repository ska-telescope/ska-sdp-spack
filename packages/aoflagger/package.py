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
    version('2.15.0', commit='7d461db725e2c044c4b5653db3aa19a30cc7466a', submodules=True)

    depends_on('casacore+python@3.3.0:', when='@2.15.0')
    depends_on('casacore+python@3.3.0:', when='@3.1.0')
    depends_on('fftw~mpi@3.3.9:')
    depends_on('boost+python+numpy@:1.65', when='@2.15.0')
    depends_on('boost+python+numpy@:1.76', when='@3.1.0')
    depends_on('libxml2')
    depends_on('lapack')
    depends_on('cfitsio')
    depends_on('lua')
    depends_on('gtkmm')
