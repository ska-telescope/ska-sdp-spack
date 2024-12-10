# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAstroplan(PythonPackage):
    
    homepage = "https://github.com/astropy/astroplan.git"
    git = "https://github.com/astropy/astroplan.git"

    license("BSD-3-Clause", checked_by="scpmw")

    version('latest', branch='main')
    version('0.10.1', commit='17d4909e8e37377b2f1e46153a204230b96367b7', preferred=True)

    depends_on("python", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
