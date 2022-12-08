# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Dal2(CMakePackage):
    """Data Access Library (DAL) provides access to the HDF5 radio astronomy
    data produced by the LOFAR telescope."""

    git      = "https://git.astron.nl/ro/dal2"

    version('v3.3.2', commit='778747d6d5406f08f0669b94ed6c4f67abb5c5a9')

    variant('python', default=False, description='Generate python bindings')

    depends_on('hdf5')
    depends_on('swig')

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define('PYTHON_BINDINGS', '+python' in spec),
        ]
        return args

