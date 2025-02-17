from spack.package import PythonPackage, depends_on, version


class PySkaSdpBenchmarkMonitor(PythonPackage):
    """BenchMon is a monitoring tool designed to collect
    hardware and software context as well as measure benchmark runs.
    """

    homepage = "https://gitlab.com/ska-telescope/sdp/ska-sdp-benchmark-monitor"
    git = "https://gitlab.com/ska-telescope/sdp/ska-sdp-benchmark-monitor.git"

    # versions
    version("main", branch="main", no_cache=True)

    depends_on("python", type=("build", "run"))
    depends_on("py-psutil", type="run")
    depends_on("py-ping3", type="run")
    depends_on("py-numpy", type="run")
    depends_on("py-matplotlib", type="run")
    depends_on("py-requests", type="run")
    depends_on("py-setuptools", type="build")
    depends_on("dool@1.3.4", type="run")
