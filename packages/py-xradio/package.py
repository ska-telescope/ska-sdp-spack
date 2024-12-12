
from spack.package import *
import os
import glob

class PyXradio(PythonPackage):

    homepage = "https://github.com/casangi/xradio"
    git = "https://github.com/casangi/xradio.git"

    license("BSD-3-Clause", checked_by="scpmw")

    version('0.0.45', commit='98f313c470900b69eb3d0f5d13904f268f1ea700')
    version('0.0.40', commit='1b08a6bb41223fe2b6a860e1648d1758d2874859')
    version('latest', branch='main')

    depends_on('py-astropy',type=("build", "run"))
    depends_on('py-dask',type=("build", "run"))
    depends_on('py-distributed',type=("build", "run"))
    depends_on('py-toolviper@0.0.2:',type=("build", "run"))
    # depends_on('py-numba@0.57.0:',type=("build", "run"))
    depends_on('py-numpy',type=("build", "run"))
    depends_on('py-s3fs@2024:',type=("build", "run"))
    depends_on('py-scipy',type=("build", "run"))
    depends_on('py-xarray',type=("build", "run"))
    depends_on('py-zarr',type=("build", "run"))
    depends_on('py-pyarrow',type=("build", "run"))
    depends_on('py-casacore@3.6.1:',type=("build", "run"))
    depends_on('py-typing-extensions',type=("build", "run"))
    depends_on('py-typeguard', type=("build", "run"))

