# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySdpPfl(PythonPackage):
    """Python bindings for SDP Processing Function Library, A collection of high-performance 
    data processing utility functions for the Square Kilometre Array."""

    homepage = "https://gitlab.com/ska-telescope/sdp/ska-sdp-func"
    url = "https://gitlab.com/ska-telescope/sdp/ska-sdp-func/-/archive/1.1.7/ska-sdp-func-1.1.7.tar.gz"
    git = "https://gitlab.com/ska-telescope/sdp/ska-sdp-func"

    # maintainers("saliei")

    license("BSD-3-Clause")

    version("develop-1.2.0", branch="main", preferred=True)
    version("1.2.0", sha256="4991003919aac8045b515cd9cd641d88fc1f886087e5d669f9e2d91b7e6d5b3d")
    version("1.1.7", sha256="b712499e9bf4b79c319b176de4450acfcd28c5edd2406bf8aac640f31db5e796")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.1.0:", type="build")

    variant("cuda", default=False, description="Build CUDA kernels")
    variant("cuda_arch", values=("6.0", "6.1", "6.2", "7.0", "7.5", "8.0", "8.6", "8.7"), \
            default="all", multi=True, description="Build for CUDA arch")
    variant("mkl", default=False, description="Build with Intel MKL support")

    depends_on("py-setuptools", type="build")
    depends_on("sdp-pfl", type=("build", "link"))
    depends_on("py-pytest", type="test")

    depends_on("cuda@7.0.0:", when="+cuda")
    depends_on("intel-oneapi-mkl@2021.1.1:", when="+mkl")

    def setup_build_environment(self, env):
        cmake_args = []

        if "+cuda" in self.spec:
            cmake_args.append("-DFIND_CUDA=ON")
            if "+cuda_arch" in self.spec:
                cmake_args.append("-DCUDA_ARCH={0}".format(";".join(self.spec["cuda_arch"].value)))
        else:
            cmake_args.append("-DFIND_CUDA=OFF")

        if "+mkl" in self.spec:
            cmake_args.append("-DFIND_MKL=ON")
        else:
            cmake_args.append("-DFIND_MKL=OFF")

        env.set("CMAKE_ARGS", " ".join(cmake_args))

    def test(self):
        pytest("-V")
