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
    depends_on('py-pandas', type=("build", "run"))
    depends_on('py-poetry-core', type=("build", "run"))
    depends_on('py-h5py', type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-dask", type=("build", "run"))
    depends_on("py-ska-sdp-func", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
