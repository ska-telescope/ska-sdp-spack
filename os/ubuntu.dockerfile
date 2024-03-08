FROM ubuntu:22.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
      bash build-essential ca-certificates coreutils curl \
      gfortran git gpg lsb-release python3 python3-pip \
      unzip zip wget && \
    rm -rf /var/lib/apt/lists/* /var/apt/cache

SHELL ["/bin/bash", "-c"]
ARG SPACK_VERSION=v0.21.0
RUN git clone --depth=1 --branch=${SPACK_VERSION} https://github.com/spack/spack.git /opt/spack
LABEL SPACK_VERSION=${SPACK_VERSION}
LABEL OS_VERSION="ubuntu:22.04"

# AST-1508: Prevent parallel builds of cfitsio, since they sometimes fail.
RUN sed -i "16i\    parallel = False" /opt/spack/var/spack/repos/builtin/packages/cfitsio/package.py

# Pre-install some packages so the test jobs become shorter.
RUN . /opt/spack/share/spack/setup-env.sh && \
    spack compiler find && \
    spack install cfitsio fftw git gsl hdf5+cxx \
      openblas threads=pthreads python py-numpy wcslib+cfitsio