FROM artefact.skao.int/ska-build-python:0.1.1

SHELL ["/bin/bash", "-c"]

ARG SPACK_BRANCH=releases/v0.23
ARG SPACK_ROOT=/spack
ARG SPACK_ENV_NAME=sdp

ARG SPACK_CACHE_VERSION=v0.22.2
ARG SPACK_E4S_MIRROR=https://cache.e4s.io/24.11
ARG SPACK_E4S_MIRROR_NAME=E4S

ARG SPACK_ADD_CMD="spack -e ${SPACK_ENV_NAME} add"
ARG SPACK_CONCRETIZE_CMD="spack -e ${SPACK_ENV_NAME} concretize -f"
ARG SPACK_INSTALL_CMD="spack -e ${SPACK_ENV_NAME} install --fail-fast"

WORKDIR /

RUN apt update -y && apt upgrade -y
RUN apt install -y gcc g++ gfortran
RUN apt install -y python3
RUN apt install -y zip unzip
RUN apt install -y git

RUN git clone --depth=2 --branch=$SPACK_BRANCH https://github.com/spack/spack.git $SPACK_ROOT
ENV PATH="${PATH}:/spack/bin"
ENV SPACK_ROOT=$SPACK_ROOT
RUN spack compiler find

RUN spack mirror add $SPACK_CACHE_VERSION https://binaries.spack.io/$SPACK_CACHE_VERSION
RUN spack mirror add $SPACK_E4S_MIRROR_NAME $SPACK_E4S_MIRROR
RUN spack buildcache keys --install --trust

RUN git clone https://gitlab.com/ska-telescope/sdp/ska-sdp-spack.git $SPACK_ROOT/var/spack/repos/ska-sdp-spack
RUN spack repo add $SPACK_ROOT/var/spack/repos/ska-sdp-spack

WORKDIR $SPACK_ROOT/var/spack/repos/ska-sdp-spack
RUN git switch hip-1120-container-image

RUN spack env create $SPACK_ENV_NAME
# COPY ./spack.yaml $SPACK_ROOT/var/spack/environments/$SPACK_ENV_NAME/spack.yaml
# NOTE: Here we avoid a for loop to make each package a separate container layer.
# TODO: Add packages as they become stable.
RUN $SPACK_ADD_CMD aoflagger;      $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
RUN $SPACK_ADD_CMD wsclean;        $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
RUN $SPACK_ADD_CMD everybeam;      $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
RUN $SPACK_ADD_CMD idg;            $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
RUN $SPACK_ADD_CMD dp3;            $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
RUN $SPACK_ADD_CMD ducc;           $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
RUN $SPACK_ADD_CMD dysco;          $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
RUN $SPACK_ADD_CMD pmt;            $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
RUN $SPACK_ADD_CMD pqxx-autotools; $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
RUN $SPACK_ADD_CMD py-ducc;        $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
RUN $SPACK_ADD_CMD rum;            $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
RUN $SPACK_ADD_CMD py-casacore;    $SPACK_CONCRETIZE_CMD; $SPACK_INSTALL_CMD
