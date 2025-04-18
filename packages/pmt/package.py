from spack.package import *


class Pmt(CMakePackage):
    """ PMT: Power Measurement Toolkit """

    homepage = "https://git.astron.nl/RD/pmt"
    git      = "https://git.astron.nl/RD/pmt"

    version('latest', branch='master', no_cache=True, deprecated=True)
    version('master', branch='master', no_cache=True)

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
            self.define('BUILD_ARDUINO_PMT', '+arduino' in spec),
	        self.define('BUILD_LIKWID_PMT', '+likwid' in spec),
	        self.define('BUILD_NVML_PMT', '+nvml' in spec),
            self.define('BUILD_PYTHON_PMT', '+python' in spec),
            self.define('BUILD_ROCM_PMT', '+rocm' in spec),
        ]
        return args

    def setup_run_environment(self, env):
        spec = self.spec
        if ('+python') in spec:
            python_version = self.spec.dependencies('python')[0].version.up_to(2)
            env.prepend_path('PYTHONPATH', join_path(self.prefix.lib, f"python{python_version}", 'site-packages'))
