# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os
import glob

class PySkaSdpDistributedSelfCalPrototype(PythonPackage):
    
    homepage = "https://gitlab.com/ska-telescope/sdp/science-pipeline-workflows/ska-sdp-distributed-self-cal-prototype"
    git = "https://gitlab.com/ska-telescope/sdp/science-pipeline-workflows/ska-sdp-distributed-self-cal-prototype.git"

    license("BSD-3-Clause", checked_by="sstansill")
    maintainers("milhazes", "sstansill", "max_m17", "mmacleod_za", "gemmadanks")

    version('0.1.0', commit='v0.1.0', submodules=True)
    version('latest', branch='main', submodules=True, preferred=True)

    depends_on("python", type=("build", "run"))
    depends_on('py-tomlkit', type=("build", "run"))
    depends_on('py-yaml', type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-dask", type=("build", "run"))
    depends_on("py-poetry-core", type=("build", "run"))
    depends_on("py-xarray", type=("build", "run"))
    depends_on("py-astropy@6:", type=("build", "run"))
    depends_on("py-ska-sdp-exec-swiftly", type=("build", "run"))
