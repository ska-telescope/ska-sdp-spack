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

    depends_on('casacore+python@3.3.0')
    depends_on('cfitsio@3.49')
    depends_on('fftw@3.3.9:')
    depends_on('boost+python+numpy@1.76.0')
    depends_on('hdf5@1.10.7')
    depends_on('libxml2')
    depends_on('lapack')
    depends_on('lua')
