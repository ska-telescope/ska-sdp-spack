# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySkaSdpFuncPython(PythonPackage):
    
    homepage = "https://gitlab.com/ska-telescope/sdp/ska-sdp-func-python"
    git = "https://gitlab.com/ska-telescope/sdp/ska-sdp-func-python"

    license("BSD-3-Clause", checked_by="scpmw")

    version('latest', branch='main', submodules=True)
    version('0.5.1', commit='46e78257e4684ed8f339e351c699d627debde6b0', submodules=True, preferred=True)

    depends_on("python", type=("build", "run"))
    depends_on('py-poetry-core', type=("build", "run"))
    depends_on('py-astropy@6.1:', type=("build", "run"))
    depends_on('py-astroplan@0.10.1:', type=("build", "run"))
    depends_on('py-ducc', type=("build", "run"))
    depends_on("py-numpy@1.26:", type=("build", "run"))
    depends_on("py-photutils@1.5:", type=("build", "run"))
    depends_on("py-scipy@1.14:", type=("build", "run"))
    depends_on("py-xarray@2024.7:", type=("build", "run"))
    depends_on("py-reproject@0.9", type=("build", "run"))
    depends_on("py-ska-sdp-datamodels@0.3.3:", type=("build", "run"))
