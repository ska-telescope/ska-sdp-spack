# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the Spack COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyExtensionHelpers(PythonPackage):
    """The extension-helpers package includes convenience helpers to
    assist with building Python packages with compiled C/Cython
    extensions. It is developed by the Astropy project but is intended
    to be general and usable by any Python package."""

    homepage = "https://github.com/astropy/astropy-helpers"
    pypi = "extension-helpers/extension-helpers-0.1.tar.gz"

    license("BSD-3-Clause")

    version("1.1.1", sha256="f95dd304a523d4ff6680d9504fa1d68a4dd03bf3bfbbe0ade4d927ed9e693f00")
    version("0.1", sha256="ac8a6fe91c6d98986a51a9f08ca0c7945f8fd70d95b662ced4040ae5eb973882")

    depends_on("c", type="build")  # generated

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools@30.3:", type="build")
