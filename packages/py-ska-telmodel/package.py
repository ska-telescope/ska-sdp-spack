
from spack.package import *

class PySkaTelmodel(PythonPackage):
    """
    Library for retrieving and working with SKA Telescope Model
    information.  What we are concerned with is enabling different SKA
    sub-systems to agree about information - such as shared
    assumptions about:

    * the physical location of telescope receptors (i.e. dishes or
      stations), or
    * configuration of the correlator and its connections to links, or
    * internal configuration templates for sub-systems

    This sort of information evolves relatively slowly and is in many
    cases too voluminous to be exchanged between systems in real time. On
    the other hand, especially for information characterising knowledge
    about the telescope, we will need to evolve it independently of the
    software development lifecycle.  For this purpose, this library
    provides:

    * Means to access versioned telescope model data
    * Schemas to check whether telescope model data is valid
    * Ways for interpret and transform telescope model information

    """
    
    homepage = "https://gitlab.com/ska-telescope/ska-telmodel"
    git = "https://gitlab.com/ska-telescope/ska-telmodel"

    license("BSD-3-Clause", checked_by="scpmw")

    version('1.19.7', commit='9537d36c7cdd23f41cd23ddf5bab3b4f89a92c3a')
    version('develop', branch='master')

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
