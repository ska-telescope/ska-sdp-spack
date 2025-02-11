# SKA SDP Spack Repository

This repository contains Spack package definitions for the Square Kilometre Array (SKA) Science Data Processor (SDP) software stack and its dependencies.

## Prerequisites

- Git
- Python 3.10 or later
- Compiler suite (e.g. GCC, or Intel OneAPI, etc.)

## Quick Start

1. Install Spack (skip if already installed):
```bash
# mind the branch, here is set to the latest release version,
# different spack version may result in different package resolutions.
git clone --depth=2 --branch=releases/v0.23 https://github.com/spack/spack.git
source spack/share/spack/setup-env.sh
spack compiler find
# if desired add cache mirrors to speedup package installations
# spack mirror add v0.23.0 https://binaries.spack.io/v0.23.0
```

2. Clone and add the SKA SDP repository:
```bash
git clone https://gitlab.com/ska-telescope/sdp/ska-sdp-spack.git
spack repo add ./ska-sdp-spack
```

3. Proceed with installing packages, e.g:
```bash
# Install WSClean with default configuration
spack install wsclean

# Install DP3 (includes aoflagger)
spack install dp3
```

- Note that we could have also created a Spack environment and then installed packages:
```bash
# Add sdp spack environment
spack env create sdp
spack env activate -p sdp
spack add dp3 
spack concretize 
spack install -v
```

Please consult [official Spack documentation](https://spack.readthedocs.io/en/latest/features.html) 
on different commands and subcommand flags.

## Version Management

### Spack Version Control
It is important to maintain consistent Spack versions across your development environment, 
especially after Spack updated its builtin concretizer. Different Spack versions may select 
different default package versions. For example:
- Spack v0.17.1 defaults to `cuda@11.5.0`
- Later versions may default to newer CUDA versions

### Package Version Specification

To install specific versions of packages:
```bash
# Install specific WSClean and IDG versions
spack install wsclean@3.5.1 ^idg@0.8.1

# Check available versions
spack info wsclean
spack info idg
```

## Common Configurations

### CUDA Support
If you encounter CUDA compatibility issues, you can specify an older CUDA version:
```bash
# Install with specific CUDA version
spack install cuda@10.0.130
spack install idg ^cuda@10.0.130
spack install wsclean ^cuda@10.0.130
```

### Default Environment
A default environment configuration is provided in `spack.yaml`. This includes:
- Standard Python packages (Astropy, SciPy)
- Radio astronomy tools (WSClean, DP3, AOFlagger)
- SKA-specific packages

To use the default environment:
```bash
spack env create sdp spack.yaml
spack env activate -p sdp
spack install
```

## Package List

Key packages available in this repository:

### Radio Astronomy Tools
- WSClean: Advanced radio astronomy imaging.
- DP3: Data processing pipeline.
- AOFlagger: RFI flagging.
- Casacore: Radio astronomy data processing library.

### SKA Packages
- py-ska-telmodel
- py-ska-sdp-datamodels
- py-ska-sdp-func-python

## Troubleshooting

### Common Issues

1. Build Failures
   - Check system dependencies.
   - Verify compiler compatibility.
   - Review build logs in `~/.spack/var/spack/builds/`.

2. Version Conflicts
   - Use `spack spec -I` to inspect dependency resolution.
   - Consider using `spack concretize --force` for testing.

### Getting Help

- Report issues on the [GitLab repository](https://gitlab.com/ska-telescope/sdp/ska-sdp-spack/-/issues)
- Consult the [Spack documentation](https://spack.readthedocs.io/)
- Check the [SKA Developer Portal](https://developer.skao.int)

## Contributing

1. Create a feature branch
2. Submit a merge request

Please follow the [SKA coding guidelines](https://developer.skao.int/en/latest/tools/codeguides.html).

## License

This project is licensed under the BSD 3-Clause "New" or "Revised" License - see the [LICENSE](LICENSE) file for details.
