FROM rockylinux:8

RUN yum update -y &&\
    yum install -y epel-release &&\
    yum update -y &&\
    yum --enablerepo epel groupinstall -y "Development Tools" &&\
    yum --enablerepo epel install -y findutils gcc-c++ gcc gcc-gfortran git gnupg2 hostname iproute make patch python3 python3-pip python3-setuptools unzip wget&&\
    dnf config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-rhel8.repo 128 &&\
    dnf install -y cuda &&\
    python3 -m pip install boto3

ARG SPACK_VERSION=v0.18.1
RUN    git clone --depth=1 --branch=${SPACK_VERSION} https://github.com/spack/spack.git /opt/spack
LABEL SPACK_VERSION=${SPACK_VERSION}
LABEL OS_VERSION="rockylinux:8"
COPY os/entrypoint.sh /opt/entrypoint.sh
RUN chmod a+x /opt/entrypoint.sh
ENTRYPOINT [ "/opt/entrypoint.sh" ]

RUN . /opt/entrypoint.sh &&\
    spack env create lofar &&\
    spack env activate lofar

COPY os/spack.yaml /opt/spack/var/spack/environments/lofar/spack.yaml
RUN . /opt/entrypoint.sh &&\ 
    export GCC_VERSION=$(gcc --version | head -n 1 | cut -f 3 -d " ") &&\
    sed -i s/GCC_VERSION/${GCC_VERSION}/ /opt/spack/var/spack/environments/lofar/spack.yaml &&\
    spack compiler find


