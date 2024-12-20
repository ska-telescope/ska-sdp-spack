
from spack.package import *
import os
import glob

class PyXradio(PythonPackage):
    """
    XRADIO (Xarray Radio Astronomy Data I/O) makes working with
    radio astronomy data in Python simple, efficient, and fun!

    Currently, XRADIO implements a draft of the Measurement Set v4.0.0
    schema, designed for storing radio interferometer and single-dish
    telescope data for offline processing.
    """

    homepage = "https://github.com/casangi/xradio"
    git = "https://github.com/casangi/xradio.git"

    license("BSD-3-Clause", checked_by="scpmw")

    version('0.0.45', commit='v0.0.45')
    version('0.0.41', commit='v0.0.41')
    version('0.0.40', commit='v0.0.40')
    version('latest', branch='main')

    # TODO: These dependencies are likely incorrect - xradio is still
    # in a fairly experimental development phase, and dependencies are
    # likely going to be revised significantly soon (Source: JW claimed
    # at the review we'd go down to 4 dependencies!)

    variant("numba", default=True, description="Add numba kernels")

    depends_on('py-astropy',type=("build", "run"))
    depends_on('py-dask',type=("build", "run"))
    depends_on('py-distributed',type=("build", "run"))
    depends_on('py-toolviper@0.0.2:',type=("build", "run"))
    depends_on('py-numba@0.57.0:',type=("build", "run"), when="+numba")
    depends_on('py-numpy',type=("build", "run"))
    depends_on('py-s3fs@2024:',type=("build", "run"))
    depends_on('py-scipy',type=("build", "run"))
    depends_on('py-xarray',type=("build", "run"))
    depends_on('py-zarr',type=("build", "run"))
    depends_on('py-pyarrow',type=("build", "run"))
    depends_on('py-casacore@3.6.1:',type=("build", "run"))
    depends_on('py-typing-extensions',type=("build", "run"))
    depends_on('py-typeguard', type=("build", "run"))

