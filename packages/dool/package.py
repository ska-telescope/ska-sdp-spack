import os
import shutil

from spack.package import Package, depends_on, run_after, version


class Dool(Package):
    """Dool is a command-line tool for monitoring various aspects of your Linux
    system, such as CPU, Memory, Network, Load Average, etc. It features a robust
    plug-in architecture for monitoring additional metrics. This is a Python3
    compatible fork of Dstat."""

    homepage = "https://github.com/scottchiefbaker/dool"
    git = "https://github.com/scottchiefbaker/dool.git"

    # Define the latest version
    version("latest", branch="master", preferred=True)

    # Python is required for execution
    depends_on("python", type=("run"))

    def install(self, spec, prefix):
        """Manually install the package by copying necessary files."""

        # Create directories in the Spack installation prefix
        bin_dir = os.path.join(prefix, "bin")
        plugin_dir = os.path.join(prefix, "share", "dool")

        os.makedirs(bin_dir, exist_ok=True)
        os.makedirs(plugin_dir, exist_ok=True)

        # Copy the main dool script to bin/
        shutil.copy("dool", bin_dir)
        os.chmod(os.path.join(bin_dir, "dool"), 0o755)  # Make it executable

        # Copy plugins to share/dool/
        for plugin in os.listdir("plugins"):
            shutil.copy(os.path.join("plugins", plugin), plugin_dir)
            os.chmod(os.path.join(plugin_dir, plugin), 0o644)  # Read-only

    @run_after("install")
    def post_install_message(self):
        print("Dool has been installed successfully.")
        print(f"To use it, add {os.path.join(self.prefix, 'bin')} to your PATH.")
