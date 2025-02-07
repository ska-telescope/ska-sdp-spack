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

    # versions
    version("1.3.4", tag="v1.3.4")
    version("master", branch="master", no_cache=True)

    # Apply patch for running dool on nodes without hyperthreading
    patch("fix_dool_cpufreq.patch", when="@1.3.4")

    depends_on("python", type=("run"))

    def install(self, spec, prefix):
        """Manually install the package by copying necessary files."""

        # Define installation directories (bin/ and plugins/ inside bin)
        bin_dir = os.path.join(prefix, "bin")
        plugin_dir = os.path.join(bin_dir, "plugins")

        os.makedirs(bin_dir, exist_ok=True)
        os.makedirs(plugin_dir, exist_ok=True)

        # Copy the main dool script to bin/
        shutil.copy("dool", bin_dir)
        os.chmod(os.path.join(bin_dir, "dool"), 0o755)

        # Copy all plugins to bin/plugins/
        for plugin in os.listdir("plugins"):
            shutil.copy(os.path.join("plugins", plugin), plugin_dir)
            os.chmod(os.path.join(plugin_dir, plugin), 0o644)
