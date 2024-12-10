# Spack package for the Python YAML parser (PyYAML)

from spack.package import *


class PyYaml(PythonPackage):
    """PyYAML is a YAML parser and emitter for Python."""

    # Git repository for py-yaml
    git = "https://github.com/yaml/pyyaml.git"

    # Use the most recent release version as the default
    version("main", branch="main")

    # If you need specific versions, you can add them here like this:
    # version("6.0", tag="6.0")

    # Define dependencies
    depends_on("py-setuptools", type="build")
    depends_on("py-cython", type="build")

    def build_args(self, spec, prefix):
        args = []
        return args
