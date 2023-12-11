# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libpowersensor(CMakePackage):
    """ This is a collection of PowerSensor implementations, based on the original PowerSensor code, """

    homepage      = "https://gitlab.com/astron-misc/libpowersensor.git"
    git      = "https://gitlab.com/astron-misc/libpowersensor.git"

    version('latest', branch='python-bindings', preferred=True)

    variant('arduino', default=False, description='Enable Arduino support')
    variant('likwid', default=False, description='Enable Likwid support')
    variant('nvml', default=False, description='Enable CUDA support')
    variant('python', default=False, description='Enable Python bindings support')
    variant('rocm', default=False, description='Enable ROCM-smi-lib support')

    depends_on('cuda', when='+nvml')
    depends_on('python', when='+python')
    depends_on('py-pybind11', when='+python')
    depends_on('rocm-smi-lib', when='+rocm')

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define('BUILD_ARDUINO_POWERSENSOR', '+arduino' in spec),
            self.define('BUILD_LIKWID_POWERSENSOR', '+likwid' in spec),
            self.define('BUILD_NVML_POWERSENSOR', '+nvml' in spec),
            self.define('BUILD_PYTHON_POWERSENSOR', '+python' in spec),
            self.define('BUILD_ROCM_POWERSENSOR', '+rocm' in spec),
        ]
        return args

    def setup_run_environment(self, env):
        spec = self.spec
        if ('+python') in spec:
            import re
            python_version = re.search(r'python@=([\d]+.[\d]+)', str(self.spec)).group(1)
            env.prepend_path('PYTHONPATH', join_path(self.prefix.lib, "python"))
