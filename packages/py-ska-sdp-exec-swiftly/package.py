
from spack.package import *

class PySkaSdpExecSwiftly(PythonPackage):
    
    homepage = "https://gitlab.com/ska-telescope/sdp/ska-sdp-exec-swiftly"
    git = "https://gitlab.com/ska-telescope/sdp/ska-sdp-exec-swiftly"

    license("BSD-3-Clause", checked_by="sstansill")

    version('1.0.0', commit='db316ec7e49808e8f6c77c55e3a7571382a3524e')
    version('develop', branch='main')

    depends_on("python@3.10:", type=("build", "run"))
    depends_on('py-distributed@2024.2:', type=("build", "run"))
    depends_on('py-dask@2024.2:', type=("build", "run"))
    depends_on('py-poetry-core', type="build")
    depends_on("py-numpy@1.26:", type=("build", "run"))
    depends_on("py-scipy@1.12:", type=("build", "run"))
    depends_on('py-h5py@3.10:', type=("build", "run"))
    depends_on("py-pandas@2.2:", type=("build", "run"))
    depends_on("py-ska-sdp-func@1.0.1:", type=("build", "run"))
