# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyCasacore(PythonPackage):
    """Python-casacore is a set of Python bindings for casacore, a c++ library used in radio astronomy."""

    homepage = "https://github.com/casacore/python-casacore"
    pypi = "python-casacore/python-casacore-3.4.0.tar.gz"

    version('3.4.0', sha256='f654781292308de70c037981f5f7f5aeb02cf980a6f1367d1c294e7b4fca42ce')

    depends_on('py-setuptools', type='build')
    depends_on('casacore+python+data')
    depends_on('cfitsio')
    depends_on('boost+python')

    def setup_build_environment(self, env):
        env.prepend_path('LD_LIBRARY_PATH', self.spec['boost'].prefix.lib)
        env.prepend_path('LD_LIBRARY_PATH', self.spec['casacore'].prefix.lib)
