from spack.package import *


class Dp3(CMakePackage):
    """LOFAR preprocessing software, including averaging,
	flagging, various kinds of calibration and more."""

    homepage = "https://dp3.readthedocs.io"
    git      = "https://git.astron.nl/RD/DP3.git"

    version('5.0', commit='v5.0', submodules=True)
    version('5.1', commit='v5.1', submodules=True)
    version('5.2', commit='v5.2', submodules=True)
    version('5.3', commit='v5.3', submodules=True)
    # 5.4 is not an actual DP3 version, however at this commit the DP3_VERSION was set to 5.4.0
    version('5.4', commit='548828e2fde1a5fc504042b6af384c398b484f79', submodules=True)
    version('6.0', commit='v6.0', submodules=True)
    version('6.1', commit='v6.1', submodules=True)
    version('6.2.1', commit='v6.2.1', submodules=True)
    version('6.3', commit='v6.3', submodules=True, preferred=True)
    version('latest', branch='master', submodules=True, no_cache=True, deprecated=True)
    version('master', branch='master', submodules=True, no_cache=True)

    variant('python', default=True, description='Enable Python support')

    depends_on('aoflagger@3.4.0', when='@latest')
    depends_on('aoflagger@3.4.0', when='@6.0:')
    depends_on('aoflagger@3.2.0', when='@5.3:5.4')
    depends_on('aoflagger@3.1.0', when='@5.0:5.2')
    depends_on('everybeam@0.6:0.7', when='@latest')
    depends_on('everybeam@0.6:0.7', when='@6.3:')
    depends_on('everybeam@0.6', when='@6.1:6.2')
    depends_on('everybeam@0.5.3', when='@6.0')
    depends_on('everybeam@0.4.0', when='@5.4')
    depends_on('everybeam@0.3.0', when='@5.3')
    depends_on('everybeam@0.3.0', when='@5.2')
    depends_on('everybeam@0.1.3', when='@5.1')
    depends_on('everybeam@0.1.1', when='@5.0')
    depends_on('openblas threads=pthreads')
    depends_on('boost+date_time+test+program_options')
    depends_on('hdf5')
    depends_on('gsl')
    depends_on('git')
    depends_on('python', when='+python')

    def setup_build_environment(self, env):
        print(self.spec.version)
        if (self.spec.satisfies('@latest') or self.spec.satisfies('@master') or
           int(str(self.spec.version.joined)) >= 52):
            env.set("OPENBLAS_NUM_THREADS", "1")

    def setup_run_environment(self, env):
        env.set("OPENBLAS_NUM_THREADS", "1")
        spec = self.spec
        if ('+python') in spec:
            python_version = self.spec.dependencies('python')[0].version.up_to(2)
            env.prepend_path('PYTHONPATH', join_path(self.prefix.lib, f"python{python_version}", 'site-packages'))
