# Getting started
```
cd /path/your-working-dir
git clone https://github.com/spack/spack.git
git clone https://github.com/HDFGroup/hdf-spack.git
git clone https://git.astron.nl/RD/schaap-spack.git
source ./spack/share/spack/setup-env.sh
spack repo add ./hdf-spack
spack repo add ./schaap-spack
```

After this initial setup, you could run `spack install wsclean`, as this will install `wsclean` and all its dependencies.
Next, you could install `dp3` seperately (wich also installs `aoflagger` as a dependency).
Note that we do not use the built-in `hdf5` package, it is broken. Instead we use `hdf5-autotools`.

Tested on CentOS 8.4 with GCC/9.3.0 (and some common system packages).

# Customization

Add compilers in `~/.spack/linux/compilers.yaml `:
```
compilers:
- compiler:
    spec: gcc@8.4.1
    paths:
      cc: /usr/bin/gcc
      cxx: /usr/bin/g++
      f77: /usr/bin/gfortran
      fc: /usr/bin/gfortran
    flags: {}
    operating_system: centos8
    target: x86_64
    modules: []
    environment: {}
    extra_rpaths: []
- compiler:
    spec: gcc@9.3.0
    paths:
      cc: /opt/ohpc/pub/compiler/gcc/9.3.0/bin/gcc
      cxx: /opt/ohpc/pub/compiler/gcc/9.3.0/bin/g++
      f77: /opt/ohpc/pub/compiler/gcc/9.3.0/bin/gfortran
      fc: /opt/ohpc/pub/compiler/gcc/9.3.0/bin/gfortran
    flags: {}
    operating_system: centos8
    target: x86_64
    modules: []
    environment: {}
    extra_rpaths: []
```
In this case (on DAS-6), we have the default CentOS GCC/8.4.1 compiler, as well as a newer GCC/9.3.0 from the OpenHPC repository.

You might also want to customize the modules that are being generated, by configuring `~/.spack/modules.yaml `:
```
modules:
  enable:
  - tcl
  tcl:
    hash_length: 0
    naming_scheme: ${COMPILERNAME}/${COMPILERVER}/${PACKAGE}/${VERSION}
    all:
      environment:
        set:
          '{name}_ROOT': '{prefix}'
    openblas:
      suffixes:
        threads=pthreads: mt
    blacklist:
    - everything you don't
    - want a modulefile for
    - is added to this list
```
