FROM ubuntu:22.04

RUN apt-get update &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y bash build-essential ca-certificates coreutils curl environment-modules gfortran git gpg lsb-release python3 python3-distutils python3-pip python3-venv unzip zip wget&&\
    apt-get install -y nvidia-cuda-toolkit &&\
    python3 -m pip install clingo &&\
    rm -rf /var/apt/cache

SHELL ["/bin/bash", "-c"]
ARG SPACK_VERSION=v0.18.1
RUN git clone --depth=1 --branch=${SPACK_VERSION} https://github.com/spack/spack.git /opt/spack
LABEL SPACK_VERSION=${SPACK_VERSION}
LABEL OS_VERSION="ubuntu:22.04"
COPY os/entrypoint.sh /opt/entrypoint.sh
RUN chmod a+x /opt/entrypoint.sh
ENTRYPOINT [ "/opt/entrypoint.sh" ]

RUN . /opt/entrypoint.sh &&\
    spack env create lofar &&\
    spack env activate lofar

COPY os/spack.yaml /opt/spack/var/spack/environments/lofar/spack.yaml
RUN . /opt/entrypoint.sh &&\ 
    export GCC_VERSION=$(gcc --version | head -n 1 | cut -f 3 -d " " | cut -f 1 -d "-" ) &&\
    sed -i s/GCC_VERSION/${GCC_VERSION}/ /opt/spack/var/spack/environments/lofar/spack.yaml &&\
    spack compiler find
