from spack.package import *


class Rum(CMakePackage):
    """ RUM: Resource Usage Monitoring """

    homepage = "https://gitlab.com/ska-telescope/sdp/ska-sdp-rum"
    git      = "https://gitlab.com/ska-telescope/sdp/ska-sdp-rum"

    version('latest', branch='main', no_cache=True, deprecated=True)
    version('main', branch='main', no_cache=True)

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
            python_version = self.spec.dependencies('python')[0].version.up_to(2)
            env.prepend_path('PYTHONPATH', join_path(self.prefix.lib, f"python{python_version}", 'site-packages'))
