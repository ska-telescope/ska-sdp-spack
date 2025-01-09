from spack.package import PythonPackage


class PySkaSdpBatchPreprocess(PythonPackage):
    """The Batch Preprocessing Pipeline prepares visibility data in MSv2 format 
    before they can be sent off for self-calibration and imaging. The stages in
    typical order of run include: Static flagging, Dynamic flagging,
    Application of calibration solutions, and Averaging of the data."""

    homepage = "https://gitlab.com/ska-telescope/sdp/science-pipeline-workflows/ska-sdp-batch-preprocess/"
    url = "https://gitlab.com/ska-telescope/sdp/science-pipeline-workflows/ska-sdp-batch-preprocess/-/archive/1.0.1/ska-sdp-batch-preprocess-1.0.1.tar.gz"
    git = "https://gitlab.com/ska-telescope/sdp/science-pipeline-workflows/ska-sdp-batch-preprocess/"

    maintainers("saliei", "vmorello")

    license("BSD 3-Clause")

    version("latest", branch="main", preferred=True)
    version("1.0.1", sha256="782fd15ea6fc64eead5968a0e3a543049ef1154f67ff8648e41f98d1b77d7243")
    version("1.0.0", sha256="c82bbb865d6321d25b6ded96b9bdd956b07273214f7e592b67ec3ac0f4f2c919")
    version("0.1.0", sha256="fe2856f4559fe132499aa12957af65fa22a2426c77d80c245eae54b7e5a85ab7")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-pyyaml@6.0.1:", type=("build", "run"))

    depends_on("py-poetry", type="build")
    depends_on("py-poetry-core", type="build")


    def setup_build_environment(self, env):
        env.set("POETRY_SOURCE_AUTH_SKAO", '')
        env.set("POETRY_REPOSITORIES_SKAO_URL", "https://artefact.skao.int/repository/pypi-internal/simple")

    def install(self, spec, prefix):
        poetry = which("poetry")
        poetry("config", "virtualenvs.create", "false")
        poetry("install", "--no-dev", "--no-interaction")
        
        super().install(spec, prefix)

    def build_args(self, spec, prefix):
        return ["--no-deps"]
