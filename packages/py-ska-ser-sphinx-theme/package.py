# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySkaSerSphinxTheme(PythonPackage):
    """A Sphinx RTD theme for SKA. Based on the sphinx-rtd-theme 
    but with extra SKA cowbell."""

    homepage = "https://gitlab.com/ska-telescope/ska-ser-sphinx-theme"
    url = "https://gitlab.com/ska-telescope/ska-ser-sphinx-theme/-/archive/0.2.0/ska-ser-sphinx-theme-0.2.0.tar.gz"
    homepage = "https://gitlab.com/ska-telescope/ska-ser-sphinx-theme"

    # maintainers("saliei")

    license("BSD-3 Clause")

    version("develop-0.2.0", branch="main")
    version("0.2.0", sha256="268adf1431b195bedbd11dad103661e4b1dda331c144bc8f0cb580f7f0f33c46", preferred=True)
    version("0.1.3", sha256="9aa3d91188d1e9fd4a61e3320573ba55e3feaabd746213189c6a44e2e53db840")
    version("0.1.2", sha256="058e79f392a8097abfdc1d815b454cd9e94207f19310d2201c9fed538153d6b1")
    version("0.1.1", sha256="05309592df56502f3cc3ca2c0616943c26cf76843ba7fd12753003feba3bdde9")

    depends_on("python@3.8.1:", type=("build", "run"))
    depends_on("py-sphinx@4.0.0:", type=("build", "run"))
    depends_on("py-sphinx-rtd-theme@2.0.0:", type=("build", "run"))
    
    depends_on("py-poetry-core", type="build")

    # Development dependencies - only if dev variant is enabled
    variant('dev', default=False, description='Install development dependencies')
    depends_on('py-black@24.4.2:', type=('build', 'run'), when='+dev')
    depends_on('py-pylint@:3.0.0', type=('build', 'run'), when='+dev')
    # depends_on('py-pylint-junit@0.3.2:', type=('build', 'run'), when='+dev')
    # depends_on('py-pytest@8.3.2:', type=('build', 'run'), when='+dev')
    # depends_on('py-pytest-cov@2.10.1:', type=('build', 'run'), when='+dev')
    # depends_on('py-isort@5.6.4:', type=('build', 'run'), when='+dev')
    depends_on('py-flake8@7.0.0:', type=('build', 'run'), when='+dev')
    depends_on('py-coverage@6.1.1:', type=('build', 'run'), when='+dev')
    depends_on('py-build@0.10.0:', type=('build', 'run'), when='+dev')


    def config_settings(self, spec, prefix):
        settings = {}
        return settings

    @property
    @llnl.util.lang.memoized
    def _output_version(self):
        spec_vers_str = str(self.spec.version.up_to(3))
        if "develop" in spec_vers_str:
            # Remove 'develop-' from the version in spack
            spec_vers_str = spec_vers_str.partition("-")[2]
        return spec_vers_str
