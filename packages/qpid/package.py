# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Qpid(CMakePackage):
    """Apache Qpid makes messaging tools that speak AMQP and support many
    languages and platforms."""

    homepage = "https://qpid.apache.org/"
    git      = "https://github.com/apache/qpid-cpp.git"

    version('1.38.0', commit='d541e4833ffbabf45a840676effd68310a4b5c88')
    version('1.39.0', commit='0f5d21861f6935ed2e4eb6e21f1d3cef19e22aa5')

    variant('qmfgen', default=False, description='Enable QMFGEN support')

    depends_on('ruby')
    depends_on('boost')

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define('INSTALL_QMFGEN', '+qmfgen' in spec),
            self.define('BUILD_TESTING', False),
            self.define('ENABLE_WARNING_ERROR', False),
        ]
        return args

