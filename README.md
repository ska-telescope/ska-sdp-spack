# Getting started
```
cd <prefix>
git clone https://github.com/spack/spack.git
git clone https://git.astron.nl/RD/schaap-spack.git
source <prefix>/share/spack/setup-env.sh
spack repo add ./schaap-spack
```

After this initial setup, you could run `spack install wsclean`, as this will install `wsclean` and all its dependencies.

Next, you could install `dp3` separately (wich also installs `aoflagger` as a dependency): `spack install dp3`.

# Example deployment
On the ASTRON side of the DAS-6 cluster, `schaap-spack` is used to deploy a set of commonly used software packages.

This system uses Rocky Linux 8.5 and has gcc/9.4.0 pre-installed using Spack. To this end, we first install gcc/9.4.0 using the system compiler (gcc/8.5.0):
```
spack install gcc@9.4.0
```
Next, we add the newly installed compiler:
```
spack compiler find
```
And use this to 'seed' the gcc/9.4.0 stack:
```
spack install gcc@9.4.0 %gcc@9.4.0
```

To initialize the Spack environment, run the following command:
```
spack env create gcc-940
```

You should now have a `<prefix>/spack/var/spack/environments/gcc-940/spack.yaml` file.
Fill it with the appropriate settings:
```
spack:
  packages:
    all:
      target: [zen2]
  specs:
  - boost@1.73.0 +filesystem+system+python+numpy
  - casacore@3.4.0 +python
  - hdf5@1.10.7 +cxx+hl+threadsafe~mpi
  - openblas threads=pthreads
  - aoflagger@3.1.0
  - cfitsio@3.49
  - dp3@5.2
  - wsclean@3.0.1
  - dysco@1.2
  - anaconda3@2021.05
  - py-astropy@4.0.1.post1
  - py-casacore@3.4.0
  - py-cmake-format@0.6.10
  - py-pandas@1.3.5
  - py-pytest@6.2.5
  - py-h5py@3.6.0~mpi
  - ninja@1.10.2
  - gcc@9.4.0
  - git+tcltk
  - py-pip
  - py-ipython
  - cmake@3.22.1
  - podman
  - py-scipy ^py-setuptools@59.4.0
  - llvm@12.0.1~compiler-rt~gold~internal_unwind~libcxx~lld~lldb~omp_as_runtime~polly
  - py-pycuda
  - py-pynvml@11.4.1
  - py-sphinx
  - doxygen+graphviz
  view: false
  concretization: together
  repos:
  - <prefix>/spack-repos/schaap-spack
  'compilers:':
  - compiler:
      spec: gcc@9.4.0
      paths:
        cc: <prefix>/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/gcc-9.4.0-v7mri5dxxclgf4hq3x6nytsnnjoaaeuo/bin/gcc
        cxx: <prefix>/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/gcc-9.4.0-v7mri5dxxclgf4hq3x6nytsnnjoaaeuo/bin/g++
        f77: <prefix>/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/gcc-9.4.0-v7mri5dxxclgf4hq3x6nytsnnjoaaeuo/bin/gfortran
        fc: <prefix>/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/gcc-9.4.0-v7mri5dxxclgf4hq3x6nytsnnjoaaeuo/bin/gfortran
      flags: {}
      operating_system: rocky8
      target: x86_64
      modules: []
      environment: {}
      extra_rpaths: []
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
```

Take note of a few specific settings:
- your target may vary, e.g. `cascadelake` instead of `zen2`
- `concretization: together` makes sure that you don't end up with duplicate packages
- we use a custom naming scheme for the (TCL) environment modules
- for consistency and convenience, every environment module has a `{name}_ROOT` variable

The only thing left to do is to run:
```
spack env activate gcc-940
spack install
```

Wait for (quite) a bit and enjoy your software!
