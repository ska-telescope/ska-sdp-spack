from spack import *

class PySkaSdpBenchmarkMonitor(PythonPackage):
    """BenchMon is a monitoring tool designed to collect 
    hardware and software context as well as measure benchmark runs. 
    """

    homepage = "https://gitlab.com/ska-telescope/sdp/ska-sdp-benchmark-monitor"
    git      = "https://gitlab.com/ska-telescope/sdp/ska-sdp-benchmark-monitor.git"

    # versions
    version('0.1.0', branch='scoop-352',commit='a6b2c099b0fad638ec7d57e7fc0433062797d70b',preferred=True)
    version('latest',branch='main') 

    depends_on('python', type=('build', 'run'))
    depends_on('py-psutil', type='run')
    depends_on('py-ping3', type='run')
    depends_on('py-numpy', type='run')
    depends_on('py-matplotlib', type='run')