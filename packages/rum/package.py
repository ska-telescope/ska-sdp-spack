# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Rum(CMakePackage):
    """ RUM: Resource Usage Monitoring """

    homepage = "https://gitlab.com/ska-telescope/sdp/ska-sdp-rum"
    git      = "https://gitlab.com/ska-telescope/sdp/ska-sdp-rum"

    version('latest', branch='main', preferred=True)

    variant('python', default=False, description='Enable Python bindings support')

    depends_on('python', when='+python')
    depends_on('py-pybind11', when='+python')

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define('BUILD_PYTHON_RUM', '+python' in spec),
        ]
        return args

    def setup_run_environment(self, env):
        spec = self.spec
        if ('+python') in spec:
            import re
            python_version = re.search(r'python@=([\d]+.[\d]+)', str(self.spec)).group(1)
            env.prepend_path('PYTHONPATH', join_path(self.prefix.lib, "python"))
