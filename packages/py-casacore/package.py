# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class PyCasacore(PythonPackage):
    """Python-casacore is a set of Python bindings for casacore, a c++ library used in radio astronomy."""

    homepage = "https://github.com/casacore/python-casacore"
    url = "https://github.com/casacore/python-casacore/archive/refs/tags/v3.6.1.tar.gz"

    # maintainers("saliei")

    license("LPGL-3.0")

    version("3.6.1", sha256="48ca6e8d09d2e822c2bf5286247362d1dfe6d99acbb381676c4b16574959bc03", preferred=True)
    version("3.5.2", sha256="ad70c8e08893eec928b3e38c099bda8863f5aa9d099fd00694ad2b0d48eba08f")
    version("3.5.1", sha256="a577233c7311f64a8048180ee82d6946fee16e0dce2976eb516784a32d8b9133")
    version("3.5.0", sha256="47ac85d47051074d64415414212c8c2cfcb49a2037f5c3d78f71ab5b162d1e8b")
    version('3.4.0', sha256="f654781292308de70c037981f5f7f5aeb02cf980a6f1367d1c294e7b4fca42ce")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("py-scikit-build-core", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("boost+python", type="build")
    depends_on("cfitsio", type="build")
    depends_on("wcslib", type="build")

    depends_on("casacore+python", type=("build", "link"))

    def setup_build_environment(self, env):
        # a hack to overcome setuptools bug in not correctly
        # recognizing correct C++ Intel compiler.
        if "%oneapi" in self.spec:
            env.set("CC", os.environ.get("CXX"))

