# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Ducc(CMakePackage):
    """Distinctly Useful Code Collection (DUCC), is a collection of basic programming 
    tools for numerical computation, including Fast Fourier Transforms, Spherical Harmonic Transforms, 
    non-equispaced Fourier transforms, as well as some concrete applications like 4pi convolution
    on the sphere and gridding/degridding of radio interferometry data. Note that this 
    package doesn't install the python interface."""

    homepage = "https://gitlab.mpcdf.mpg.de/mtr/ducc"
    url = "https://gitlab.mpcdf.mpg.de/mtr/ducc.git"
    git = "https://gitlab.mpcdf.mpg.de/mtr/ducc.git"

    # maintainers("saliei")

    license("Affero General Public License v1.0")

    version("develop-0.34.0", branch="ducc0", preferred=True)

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake", type="build")

    def cmake_args(self):
        args = []
        args.append("-DDUCC_USE_THREADS=True")
        return args

    @property
    @llnl.util.lang.memoized
    def _output_version(self):
        spec_vers_str = str(self.spec.version.up_to(3))
        if "develop" in spec_vers_str:
            # Remove 'develop-' from the version in spack
            spec_vers_str = spec_vers_str.partition("-")[2]
        return spec_vers_str

