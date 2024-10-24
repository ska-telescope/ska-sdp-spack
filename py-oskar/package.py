# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOskar(PythonPackage):
    """Python bindings for OSKAR. A GPU accelerated simulator for the Square Kilometre Array."""

    homepage = "https://github.com/OxfordSKA/OSKAR"
    url = "https://github.com/OxfordSKA/OSKAR/archive/refs/tags/2.8.3.tar.gz"

    # maintainers("saliei", "fdulwich")

    license("BSD-3-Clause")

    version("2.8.3", sha256="828fe0ff72019bec3b6fa10a3928f9aa2aa1a5c6a4a8d5643364cfd6ddd50fac", preferred=True)
    version("2.8.2", sha256="f28ae5afc85f28df1636820cc97bb833fd53cff517c3bf0c27500a71bb66c4e3")
    version("2.8.1", sha256="218c841726d4dd376565a3ddfa967ef0c7e2b0a0779611a54307f4b4ab975ed5")
    version("2.8.0", sha256="2fdaf1d4a06bcb66ee580a4baf084bd3187dfa123b4ee036a5c9328184b1d606")
    version("2.7.6", sha256="c53e40ad3aae4747c480b220deb71bd457b172d1029e7f1f323b568a74d0e075")
    version("2.7.5", sha256="fc4c781f2d758e2a5398bff1ad5ecb6fa1cb64e1936e6753185d02734ec870a3")
    version("2.7.0", sha256="91bf49437bbfaae2e7e846799a32db990de0b569fbe185446ac0e9a2b54c84c7")
    version("2.6.1", sha256="5b9a4cdbceaebf91ffa3bb7fb086bc69417e085246fea4b269641710d0dc515d")
    version("2.6.0", sha256="57b400476bbbe502f6f967dc6613ea3f2158ce8c544c8d8af1502089cec226fc")


    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@:2.0.0", type=("build"))
    depends_on("oskar", type=("build", "link"))

    @property
    def build_directory(self):
        return join_path(self.stage.source_path, 'python')
    
    def setup_build_environment(self, env):
        oskar_prefix = self.spec["oskar"].prefix
        env.set("OSKAR_INC_DIR", join_path(oskar_prefix, "include"))
        env.set("OSKAR_LIB_DIR", join_path(oskar_prefix, "lib"))
