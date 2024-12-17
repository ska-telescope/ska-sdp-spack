# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySkaSdpExecSwiftly(PythonPackage):
    
    homepage = "https://gitlab.com/ska-telescope/sdp/ska-sdp-exec-swiftly"
    git = "https://gitlab.com/ska-telescope/sdp/ska-sdp-exec-swiftly"

    license("BSD-3-Clause", checked_by="sstansill")

    version('latest', branch='main', submodules=True, preferred=True)

    depends_on("python", type=("build", "run"))
    depends_on('py-distributed@2024.2:', type=("build", "run"))
    depends_on('py-dask@1024.2:', type=("build", "run"))
    depends_on('py-poetry-core', type="build")
    depends_on("py-numpy@1.26:", type=("build", "run"))
    depends_on("py-scipy@1.12:", type=("build", "run"))
    depends_on('py-h5py@3.10:', type=("build", "run"))
    depends_on("py-pandas@2.2:", type=("build", "run"))
    depends_on("py-ska-sdp-func@1.0.1:", type=("build", "run"))
