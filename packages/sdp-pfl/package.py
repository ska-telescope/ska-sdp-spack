# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class SdpPfl(CMakePackage):
    """SDP Processing Function Library is a collection of high-performance data processing utility functions 
    for the Square Kilometre Array."""

    homepage = "https://gitlab.com/ska-telescope/sdp/ska-sdp-func"
    url = "https://gitlab.com/ska-telescope/sdp/ska-sdp-func/-/archive/1.1.7/ska-sdp-func-1.1.7.tar.gz"
    git = "https://gitlab.com/ska-telescope/sdp/ska-sdp-func"

    # maintainers("saliei")

    license("BSD-3-Clause")

    version("develop-1.1.7", branch="main", preferred=True)
    version("1.1.7", sha256="b712499e9bf4b79c319b176de4450acfcd28c5edd2406bf8aac640f31db5e796")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.1.0:", type="build")
    
    variant("cuda", default=False, description="Build CUDA kernels")
    variant("cuda_arch", values=("6.0", "6.1", "6.2", "7.0", "7.5", "8.0", "8.6", "8.7"), \
            default="all", multi=True, description="Build for CUDA arch")
    variant("mkl", default=False, description="Build with Intel MKL support")

    depends_on("cuda@7.0.0:", when="+cuda")
    depends_on("intel-oneapi-mkl@2021.1.1:", when="+mkl")
    
    def cmake_args(self):
        args = []

        if "+cuda" in self.spec:
            args.append("-DFIND_CUDA=ON")
            if "+cuda_arch" in self.spec:
                args.append("-DCUDA_ARCH={0}".format(";".join(self.spec["cuda_arch"].value)))
        else:
            args.append("-DFIND_CUDA=OFF")

        if "+mkl" in self.spec:
            args.append("-DFIND_MKL=ON")
        else:
            args.append("-DFIND_MKL=OFF")

        return args

    @property
    @llnl.util.lang.memoized
    def _output_version(self):
        spec_vers_str = str(self.spec.version.up_to(3))
        if "develop" in spec_vers_str:
            # Remove 'develop-' from the version in spack
            spec_vers_str = spec_vers_str.partition("-")[2]
        return spec_vers_str

    def test(self):
        with working_dir(self.build_directory):
            ctest("-V")
