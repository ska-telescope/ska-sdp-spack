from spack.package import PythonPackage, depends_on, version

class Dool(Package):
    """Dool is a command-line tool for monitoring various aspects of your Linux 
    system, such as CPU, Memory, Network, Load Average, etc. It features a robust 
    plug-in architecture for monitoring additional metrics. This is a Python3 
    compatible fork of Dstat."""

    homepage = "https://github.com/scottchiefbaker/dool"
    git      = "https://github.com/scottchiefbaker/dool.git"

    # Specify versions
    version('latest', branch='master', preferred=True)
    
    def install(self, spec, prefix):
        """Since the repository contains ready-to-use scripts, we simply clone it into the prefix."""
        install_tree('.', prefix)
