# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySkaTelmodel(PythonPackage):
    
    homepage = "https://gitlab.com/ska-telescope/ska-telmodel"
    git = "https://gitlab.com/ska-telescope/ska-telmodel"

    license("BSD-3-Clause", checked_by="scpmw")

    version('latest', branch='master')
    version('1.19.7', commit='9537d36c7cdd23f41cd23ddf5bab3b4f89a92c3a', preferred=True)

    depends_on("python", type=("build", "run"))
    depends_on('py-poetry-core', type=("build", "run"))
    depends_on('py-schema@0.7.5:', type=("build", "run"))
    depends_on('py-appdirs@1.4.4:', type=("build", "run"))
    depends_on('py-toolz@0.12.0:', type=("build", "run"))
    depends_on('py-pyyaml@6.0:', type=("build", "run"))
    depends_on('py-overrides@7.3:', type=("build", "run"))
    depends_on('py-gitpython@3.1:', type=("build", "run"))
    depends_on('py-python-gitlab@3.8:', type=("build", "run"))
    depends_on('py-tomli@2.0:', type=("build", "run"))
    depends_on('py-filelock@3.12:', type=("build", "run"))
    depends_on('py-prettytable@3.7:', type=("build", "run"))
    depends_on('py-requests@2.32:', type=("build", "run"))
    depends_on('py-jsonschema@4.0:', type=("build", "run"))
