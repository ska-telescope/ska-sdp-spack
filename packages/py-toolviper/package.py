
from spack.package import *
import os
import glob

class PyToolviper(PythonPackage):

    homepage = "https://github.com/casangi/toolviper"
    git = "https://github.com/casangi/toolviper.git"

    license("BSD-3-Clause", checked_by="scpmw")

    version('0.0.2', commit='28fb90de58a307f5526c7873c8f2238b201b0640', preferred=True)
    version('latest', branch='main')

    depends_on('py-cerberus',type=("build", "run"))
    depends_on('py-dask',type=("build", "run"))
    # depends_on('py-dask-jobqueue',type=("build", "run"))
    depends_on('py-distributed',type=("build", "run"))
    # depends_on('py-numba@0.57.0:',type=("build", "run"))
    depends_on('py-psutil',type=("build", "run"))
    depends_on('py-ipywidgets',type=("build", "run"))
    depends_on('py-rich',type=("build", "run"))
    depends_on('py-tqdm',type=("build", "run"))
    depends_on('py-zarr',type=("build", "run"))
    depends_on('py-pyarrow',type=("build", "run"))
