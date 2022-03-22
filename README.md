# Initial setup
First, create a folder (change `<prefix>` with a name of your choice) and change directory it:

```
mkdir <prefix>
cd <prefix>
```

If `spack` is already installed, you can skip cloning it (**remember** to source its environment):
```
git clone https://github.com/spack/spack.git
source ./spack/share/spack/setup-env.sh
```
The above command will clone Spack in the directory you have created beforehand (you can clone it in a different directory).

Clone this repository and add it to `spack`:
```
git clone https://git.astron.nl/RD/schaap-spack.git
spack repo add ./schaap-spack
```

After this initial setup, you could run `spack install wsclean`, as this will install `wsclean` and all its dependencies.

Next, you could install `dp3` separately (which also installs `aoflagger` as a dependency): `spack install dp3`.

# Additional notes
- It is crucial to fix the Spack version to have identical software versions. Different Spack versions will have different preferred versions of packages, e.g Spack v0.17.1 will install `cuda@11.5.0`, while the latest Spack version may install `cuda@11.6.1`. For more information on how to deploy WSClean and IDG using Spack, see the [wiki](https://git.astron.nl/RD/schaap-spack/-/wikis/Reproducible-SW-environment-with-Spack).
- The steps mentioned above will install the latest version (master branch) on WSClean and IDG. If you want to install the latest stable release. Check the ones available with `spack info <module_name>`, where `<module_name>`, can be `wsclean` or `idg`.
For example:
```
spack install wsclean@3.0.1 ^idg@0.8.1
```

- On certain systems, some specific package versions (for instance for CUDA) may cause issues. A workaround is to use another (older) version, e.g.:
```
spack install cuda@10.0.130
spack install idg ^cuda@10.0.130
spack install wsclean ^cuda@10.0.130
```
