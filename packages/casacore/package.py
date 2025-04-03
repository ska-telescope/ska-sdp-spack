# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Casacore(CMakePackage):
    """A suite of c++ libraries for radio astronomy data processing."""

    homepage = "https://github.com/casacore/casacore"
    git = "https://github.com/casacore/casacore.git"

    # TODO: support multiple spack versions (maintainers option)
    # spack version > 18.1 changed the maintainers syntax
    # maintainers("mpokorny")
    version("3.7.1")
    version("3.6.1")
    version("3.5.0")
    version("3.4.0")
    version("3.3.0")
    version("3.2.0")
    version("3.1.2")
    version("3.1.1")
    version("3.1.0")
    version("3.0.0")
    version("2.4.1")

    depends_on("cmake@3.7.1:", type="build")

    variant("adios2", default=False, description="Build ADIOS2 support")
    variant("dysco", default=True, when="@3.5.0:", description="Build Dysco storage manager")
    variant("fftpack", default=False, description="Build FFTPack")
    variant("hdf5", default=False, description="Build HDF5 support")
    variant("mpi", default=False, description="Use MPI for parallel I/O")
    variant("openmp", default=False, description="Build OpenMP support")
    variant("python", default=False, description="Build python support")
    variant("readline", default=True, description="Build readline support")
    variant("shared", default=True, description="Build shared libraries")
    variant("tablelocking", default=True, description="Enable table locking")
    variant("threads", default=True, description="Use mutex thread synchronization")
    variant("data", default=False, description="Download WSRT measures archive from the ASTRON FTP server")

    # Force dependency on readline in v3.2 and earlier. Although the
    # presence of readline is tested in CMakeLists.txt, and casacore
    # can be built without it, there's no way to control that
    # dependency at build time; since many systems come with readline,
    # it's better to explicitly depend on it here always.
    depends_on("readline", when="@:3.2.0")
    depends_on("readline", when="+readline")
    depends_on("flex", type="build")
    depends_on("bison", type="build")
    depends_on("blas")
    depends_on("lapack")
    depends_on("cfitsio")
    depends_on("wcslib@4.20:+cfitsio")
    depends_on("fftw@3.0.0: precision=float,double", when="@3.4.0:")
    depends_on("fftw@3.0.0: precision=float,double", when="~fftpack")
    depends_on("sofa-c", type="test")
    depends_on("hdf5", when="+hdf5")
    depends_on("adios2+mpi", when="+adios2")
    depends_on("mpi", when="+mpi")
    depends_on("python@2.6:", when="+python")
    depends_on("boost +python", when="+python")
    depends_on("boost +system +filesystem", when="+dysco")
    depends_on("py-numpy", when="+python")
    depends_on("gsl", when="+dysco")
    depends_on("tar", when="+data")

    conflicts("~mpi", when="+adios2")
    conflicts("+tablelocking", when="+mpi")
    conflicts("~threads", when="+openmp")

    patch("gcc13.patch", when="%gcc@13:")
    patch("boost.patch", when="@:3.6.0")
    patch("intelLLVM.patch", when="%oneapi")

    def cmake_args(self):
        args = []
        spec = self.spec

        args.append(self.define_from_variant("BUILD_DYSCO", "dysco"))
        args.append(self.define_from_variant("ENABLE_TABLELOCKING", "tablelocking"))
        args.append(self.define_from_variant("ENABLE_SHARED", "shared"))
        args.append(self.define_from_variant("USE_THREADS", "threads"))
        args.append(self.define_from_variant("USE_OPENMP", "openmp"))
        args.append(self.define_from_variant("USE_READLINE", "readline"))
        args.append(self.define_from_variant("USE_HDF5", "hdf5"))
        args.append(self.define_from_variant("USE_ADIOS2", "adios2"))
        args.append(self.define_from_variant("USE_MPI", "mpi"))
        args.append("-DPORTABLE=ON")  # let Spack determine arch build flags

        # fftw3 is required by casacore starting with v3.4.0, but the
        # old fftpack is still available. For v3.4.0 and later, we
        # always require FFTW3 dependency with the optional addition
        # of FFTPack. In older casacore versions, only one of FFTW3 or
        # FFTPack can be selected.
        if spec.satisfies("@3.4.0:"):
            if spec.satisfies("+fftpack"):
                args.append("-DBUILD_FFTPACK_DEPRECATED=YES")
        else:
            args.append(self.define("USE_FFTW3", spec.satisfies("~fftpack")))

        # Python2 and Python3 binding
        if spec.satisfies("~python"):
            args.extend(["-DBUILD_PYTHON=NO", "-DBUILD_PYTHON3=NO"])
        elif spec.satisfies("^python@3.0.0:"):
            args.extend(["-DBUILD_PYTHON=NO", "-DBUILD_PYTHON3=YES"])
        else:
            args.extend(["-DBUILD_PYTHON=YES", "-DBUILD_PYTHON3=NO"])

        args.append("-DBUILD_TESTING=OFF")
        return args

    def patch(self):
        # Download WSRT measures archive from the ASTRON FTP server and copy it to the {self.prefix}/share/casacore/data/ path
        spec = self.spec
        if spec.satisfies("+data"):
            os.system(f"wget -nv -O {self.prefix}/WSRT_Measures.ztar ftp://ftp.astron.nl/outgoing/Measures/WSRT_Measures.ztar")
            os.system(f"mkdir -p {self.prefix}/share/casacore/data/")
            os.system(f"tar xfz {self.prefix}/WSRT_Measures.ztar -C {self.prefix}/share/casacore/data/")
        # Rely on CMake ability to find hdf5, available since CMake 3.7.X
        if os.path.exists("cmake/FindHDF5.cmake"):
            os.remove("cmake/FindHDF5.cmake")
