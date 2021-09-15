To get started:
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
Note that we do not use the builtin `hdf5` package, it is broken. Instead we use `hdf5-autotools`.

Tested on CentOS 8.4 with GCC/9.3.0 (and some common system packages).
