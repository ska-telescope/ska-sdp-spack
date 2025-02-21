
from spack.package import *


class PySkaSdpInstrumentalCalibration(PythonPackage):
    """Batch instrumental calibration pipelines for the SKA SDP. 
    This project contains the functions and scripts needed to generate the initial calibration 
    products during standard SKA batch processing. It includes processing functions to prepare, 
    model and calibrate a visibility dataset, data handling functions for parallel processing, 
    and high level pipeline scripts and notebooks."""

    homepage = "https://gitlab.com/ska-telescope/sdp/science-pipeline-workflows/ska-sdp-instrumental-calibration"
    git = "https://gitlab.com/ska-telescope/sdp/science-pipeline-workflows/ska-sdp-instrumental-calibration"

    license("BSD 3-Clause")

    version('develop', branch='main')
    version('0.1.5', commit="39c962f7d4c79f829797041a6999e5d657b3008b", preferred=True)

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-poetry-core", type="build")

    depends_on("py-astropy@6.1:", type=("build", "run"))
    depends_on("py-distributed@2024.7.1:", type=("build", "run"))
    depends_on("everybeam@0.6:", type=("build", "run"))
    depends_on("py-numpy@1.26:", type=("build", "run"))
    depends_on("py-matplotlib@3.8.3:", type=("build", "run"))
    depends_on("py-ska-sdp-datamodels@0.3.3:", type=("build", "run"))
    depends_on("py-casacore@3.5:", type=("build", "run"))
    depends_on("py-ska-sdp-func@1.2.0:", type=("build", "run"))
    depends_on("py-ska-sdp-func-python@0.5.1:", type=("build", "run"))
    depends_on("py-xarray@2024.7.0:", type=("build", "run"))

