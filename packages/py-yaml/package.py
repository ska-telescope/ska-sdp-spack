# Spack package for the Python YAML parser (PyYAML)

from spack.package import *


class PyYaml(PythonPackage):
    """PyYAML is a YAML parser and emitter for Python."""

    # Git repository for py-yaml
    homepage = "https://github.com/yaml/pyyaml"
    pypi = "pyyaml/pyyaml-6.0.2.tar.gz"

    version(
        "6.0.2",
        sha256="d584d9ec91ad65861cc08d42e834324ef890a082e591037abe114850ff7bbc3e",
    )
    version("main", branch="main")

    # Define dependencies
    depends_on("python", type=("build", "run"))
    depends_on("py-wheel", type="build")
    depends_on("py-cython", type="build")
    depends_on("py-cython@3.0:", type="build", when="^python@3.13:")
