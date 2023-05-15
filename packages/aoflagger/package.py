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
    version('3.2.0', commit='34f04470b831a217a94d89a0e65dbd7649a3852b', submodules=True)

    variant('gui', default=False, description='Build rfigui and aoqplot tools')

    depends_on('casacore+data')
    depends_on('cfitsio')
    depends_on('fftw')
    depends_on('boost+python+numpy')
    depends_on('hdf5@:1.10.7')
    depends_on('libxml2')
    depends_on('lapack')
    depends_on('lua')
    depends_on('cairo')
    depends_on('git')

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define('ENABLE_GUI', '+gui' in spec),
        ]
        return args
