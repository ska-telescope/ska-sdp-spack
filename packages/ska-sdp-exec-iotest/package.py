# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

from spack import *

class SkaSdpExecIotest(CMakePackage):
    """The I/O test is an prototype distributed visibility prediction pipeline,
       implementing the SwiFTly algorithm to generate data quickly."""

    homepage = "https://developer.skao.int/projects/ska-sdp-exec-iotest/en/latest/index.html"
    git      = "https://gitlab.com/ska-telescope/sdp/ska-sdp-exec-iotest.git"

    version('latest', branch='master', preferred=True)

    patch('iotest-fixes.patch', when='@latest')

    variant('mkl', default=False,
            description='Enable MKL support for FFTs')

    depends_on('fftw')
    depends_on('intel-oneapi-mkl', when='+mkl')
    depends_on('hdf5')
    depends_on('openmpi')
    depends_on('python')

