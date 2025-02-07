from spack.package import PythonPackage


class PyRapidsDependencyFileGenerator(PythonPackage):
    """
    rapids-dependency-file-generator is a Python CLI tool 
    that generates conda environment.yaml files and requirements.txt 
    files from a single YAML file, typically named dependencies.yaml.
    """

    homepage = "https://github.com/rapidsai/dependency-file-generator"
    git = "https://github.com/rapidsai/dependency-file-generator"
    url = "https://github.com/rapidsai/\
    dependency-file-generator/archive/refs/tags/v1.17.1.tar.gz"

    version("main", branch="main")
    version("1.17.1",
            sha256=\
            "f0b728097d353630dcdb75694cd443e8510beb0e1aca7f3deb1a3ac2262cfd0c",
            preferred=True)
    version("1.17.0",
            sha256=\
            "29b54385a6e14f4ee36a9719a0702a6c3929aabbd55f39db65a486050425b2ce")
    version("1.16.0",
            sha256=\
            "b49989947a8e9e7f722762758d536f74cc2f72d680d3939da225d58a36c235df")

    depends_on("python", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-jsonschema@3.0.0:", type=("build", "run"))
    depends_on("py-tomlkit", type=("build", "run"))
