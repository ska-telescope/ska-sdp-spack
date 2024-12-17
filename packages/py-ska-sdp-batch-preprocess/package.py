# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySkaSdpBatchPreprocess(PythonPackage):
    """The Batch Preprocessing Pipeline prepares visibility data in MSv2 format 
    before they can be sent off for self-calibration and imaging. The stages in 
    typical order of run include: Static flagging, Dynamic flagging, 
    Application of calibration solutions, and Averaging of the data."""

    homepage = "https://gitlab.com/ska-telescope/sdp/science-pipeline-workflows/ska-sdp-batch-preprocess/"
    url = "https://gitlab.com/ska-telescope/sdp/science-pipeline-workflows/ska-sdp-batch-preprocess/-/archive/1.0.1/ska-sdp-batch-preprocess-1.0.1.tar.gz"
    git = "https://gitlab.com/ska-telescope/sdp/science-pipeline-workflows/ska-sdp-batch-preprocess/"

    # maintainers("saliei")

    license("BSD 3-Clause")

    version("develop-1.0.1", branch="main", preferred=True)
    version("1.0.1", sha256="782fd15ea6fc64eead5968a0e3a543049ef1154f67ff8648e41f98d1b77d7243")
    version("1.0.0", sha256="c82bbb865d6321d25b6ded96b9bdd956b07273214f7e592b67ec3ac0f4f2c919")
    version("0.1.0", sha256="fe2856f4559fe132499aa12957af65fa22a2426c77d80c245eae54b7e5a85ab7")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-poetry", type="build")
    depends_on("py-pip", type="build")
    depends_on("python-venv", type="run")

    def install(self, spec, prefix):
        pass


