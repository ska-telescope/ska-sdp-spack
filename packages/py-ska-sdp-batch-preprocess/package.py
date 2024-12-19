# Copyright (c) 2024, The Spack Project Developers
from spack.package import *

class SkaSDPBatchPreprocessDev(PythonPackage):
    """The Batch Preprocessing Pipeline prepares visibility data in MSv2 format 
	before they can be sent off for self-calibration and imaging. The stages in
    typical order of run include: Static flagging, Dynamic flagging,
    Application of calibration solutions, and Averaging of the data."""

    homepage = "https://gitlab.com/ska-telescope/sdp/science-pipeline-workflows/ska-sdp-batch-preprocess/"
    url = "https://gitlab.com/ska-telescope/sdp/science-pipeline-workflows/ska-sdp-batch-preprocess/-/archive/1.0.1/ska-sdp-batch-preprocess-1.0.1.tar.gz"
    git = "https://gitlab.com/ska-telescope/sdp/science-pipeline-workflows/ska-sdp-batch-preprocess/"

    # maintainers("saliei")

    license("BSD 3-Clause")

    version("develop-1.0.1", branch="main", preferred=True)
    version("1.0.1", sha256="782fd15ea6fc64eead5968a0e3a543049ef1154f67ff8648e41f98d1b77d7243")
    version("1.0.0", sha256="c82bbb865d6321d25b6ded96b9bdd956b07273214f7e592b67ec3ac0f4f2c919")
    version("0.1.0", sha256="fe2856f4559fe132499aa12957af65fa22a2426c77d80c245eae54b7e5a85ab7")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-poetry", type="build")
	depends_on("py-poetry-core", type="build")
    depends_on("py-pip", type="build")
    depends_on("python-venv", type="run")

    # Development dependencies - only if dev variant is enabled
    variant("dev", default=False, description="Install development dependencies")
    depends_on("py-black@22.3.0:", type=("build", "run"), when="+dev")
    depends_on("py-pylint@2.8.2:", type=("build", "run"), when="+dev")
    depends_on("py-pylint-junit@0.3.2:", type=("build", "run"), when="+dev")
    depends_on("py-pytest@8.3.2:", type=("build", "run"), when="+dev")
    depends_on("py-pytest-cov@2.10.1:", type=("build", "run"), when="+dev")
    depends_on("py-isort@5.6.4:", type=("build", "run"), when="+dev")
    depends_on("py-flake8@3.9.2:", type=("build", "run"), when="+dev")
    depends_on("py-coverage@6.1.1:", type=("build", "run"), when="+dev")
    depends_on("py-build@0.10.0:", type=("build", "run"), when="+dev")

    # Documentation dependencies - only if docs variant is enabled
    variant('docs', default=False, description='Install documentation dependencies')
    depends_on('py-sphinx@7.0.0:', type=('build', 'run'), when='+docs')
    depends_on('py-ska-ser-sphinx-theme@0.2.0:', type=('build', 'run'), when='+docs')
    depends_on('py-recommonmark@0.7.1:', type=('build', 'run'), when='+docs')

    def setup_build_environment(self, env):
        env.set('POETRY_SOURCE_AUTH_SKAO', '')
        env.set('POETRY_REPOSITORIES_SKAO_URL', 'https://artefact.skao.int/repository/pypi-internal/simple')

    def install(self, spec, prefix):
        poetry = which('poetry')
        poetry('config', 'virtualenvs.create', 'false')
        poetry('install', '--no-dev', '--no-interaction')
        
        if '+dev' in spec:
            poetry('install', '--with', 'dev', '--no-interaction')
        if '+docs' in spec:
            poetry('install', '--with', 'docs', '--no-interaction')
        
        super().install(spec, prefix)

    def build_args(self, spec, prefix):
        return ['--no-deps']

    @property
    @llnl.util.lang.memoized
    def _output_version(self):
        spec_vers_str = str(self.spec.version.up_to(3))
        if "develop" in spec_vers_str:
            # Remove 'develop-' from the version in spack
            spec_vers_str = spec_vers_str.partition("-")[2]
        return spec_vers_str
