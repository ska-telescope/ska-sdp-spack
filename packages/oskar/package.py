# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Oskar(CMakePackage):
    """A GPU accelerated simulator for the Square Kilometre Array."""

    homepage = "https://github.com/OxfordSKA/OSKAR"
    url = "https://github.com/OxfordSKA/OSKAR/archive/refs/tags/2.8.3.tar.gz"

    # maintainers("saliei", "fdulwich")

    license("BSD-3-Clause")

    version("2.8.3", sha256="828fe0ff72019bec3b6fa10a3928f9aa2aa1a5c6a4a8d5643364cfd6ddd50fac")
    version("2.8.2", sha256="f28ae5afc85f28df1636820cc97bb833fd53cff517c3bf0c27500a71bb66c4e3")
    version("2.8.1", sha256="218c841726d4dd376565a3ddfa967ef0c7e2b0a0779611a54307f4b4ab975ed5")
    version("2.8.0", sha256="2fdaf1d4a06bcb66ee580a4baf084bd3187dfa123b4ee036a5c9328184b1d606")
    version("2.7.6", sha256="c53e40ad3aae4747c480b220deb71bd457b172d1029e7f1f323b568a74d0e075")
    version("2.7.5", sha256="fc4c781f2d758e2a5398bff1ad5ecb6fa1cb64e1936e6753185d02734ec870a3")
    version("2.7.0", sha256="91bf49437bbfaae2e7e846799a32db990de0b569fbe185446ac0e9a2b54c84c7")
    version("2.6.1", sha256="5b9a4cdbceaebf91ffa3bb7fb086bc69417e085246fea4b269641710d0dc515d")
    version("2.6.0", sha256="57b400476bbbe502f6f967dc6613ea3f2158ce8c544c8d8af1502089cec226fc")

    depends_on("cmake@3.1.0:", type="build")

    variant("cuda", default=False, description="Build CUDA kernels")
    variant("cuda_arch", values=("2.0", "2.1", "3.0", "3.2", "3.5", "3.7", "5.0", "5.2", \
            "6.0", "6.1", "6.2", "7.0", "7.5", "8.0", "8.6", "8.7"), default="all", multi=True, 
        description="Build for CUDA arch")
    variant("opencl", default=False, description="Experimental support for OpenCL")
    variant("casacore", default=False, description="Required to use CASA Measurement Sets")
    variant("hdf5", default=False, description="Required to use HDF5 files")
    variant("qt", default=False, description="Build graphical user interface")
    
    depends_on("cuda@7.0.0:", when="+cuda")
    depends_on("casacore@2.0.0:", when="+casacore")
    depends_on("hdf5@1.10.0:", when="+hdf5")
    depends_on("qt@5.0.0:", when="+qt")

    def cmake_args(self):
        args = []
        
        if "+cuda" in self.spec:
            args.append("-DFIND_CUDA=ON")
            args.append("-DCUDA_ARCH={0}".format(";".join(self.spec["cuda_arch"].value)))
        else:
            args.append("-DFIND_CUDA=OFF")

        if "+opencl" in self.spec:
            args.append("-DFIND_OPENCL=ON")
        else:
            args.append("-DFIND_OPENCL=OFF")

        if "+casacore" in self.spec:
            casacore_prefix = self.spec["casacore"].prefix
            args.append("-DCASACORE_LIB_DIR={0}/lib".format(casacore_prefix))
            args.append("-DCASACORE_INC_DIR={0}/include".format(casacore_prefix))

        return args

    def test(self):
        with working_dir(self.build_directory):
            ctest("-V")
