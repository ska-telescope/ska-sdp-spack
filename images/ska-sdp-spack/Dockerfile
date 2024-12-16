FROM artefact.skao.int/ska-build-python:0.1.1

SHELL ["/bin/bash", "-c"]

ARG SPACK_BRANCH=releases/v0.23
ARG SPACK_ROOT=/spack
ARG SPACK_ENV_NAME=sdp

ARG SPACK_CACHE_VERSION=v0.23.0
ARG SPACK_E4S_MIRROR=https://cache.e4s.io/24.11
ARG SPACK_E4S_MIRROR_NAME=E4S

ARG SPACK_CONCRETIZE_CMD="spack concretize -f"
ARG SPACK_INSTALL_CMD="spack install --fail-fast"

WORKDIR /

RUN apt update -y && apt upgrade -y
RUN apt install -y gcc g++ gfortran
RUN apt install -y zip unzip
RUN apt install -y git

RUN git clone --depth=2 --branch=$SPACK_BRANCH https://github.com/spack/spack.git $SPACK_ROOT
ENV PATH="${PATH}:/spack/bin"
ENV SPACK_ROOT=$SPACK_ROOT
RUN spack compiler find
RUN spack env create $SPACK_ENV_NAME

RUN git clone https://gitlab.com/ska-telescope/sdp/ska-sdp-spack.git $SPACK_ROOT/var/spack/repos/ska-sdp-spack
RUN spack repo add $SPACK_ROOT/var/spack/repos/ska-sdp-spack

RUN spack mirror add $SPACK_CACHE_VERSION https://binaries.spack.io/$SPACK_CACHE_VERSION
RUN spack mirror add $SPACK_E4S_MIRROR_NAME $SPACK_E4S_MIRROR
RUN spack buildcache keys --install --trust

# COPY ./spack.yaml $SPACK_ROOT/var/spack/environments/$SPACK_ENV_NAME/spack.yaml
# Here we avoid a for loop to make each package a separate container layer
RUN spack -e $SPACK_ENV_NAME add idg;         $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
RUN spack -e $SPACK_ENV_NAME add dp3;         $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
RUN spack -e $SPACK_ENV_NAME add aoflagger;   $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
RUN spack -e $SPACK_ENV_NAME add dal2;        $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
RUN spack -e $SPACK_ENV_NAME add ducc;        $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
RUN spack -e $SPACK_ENV_NAME add dysco;       $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
RUN spack -e $SPACK_ENV_NAME add everybeam;   $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
RUN spack -e $SPACK_ENV_NAME add pmt;         $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD

