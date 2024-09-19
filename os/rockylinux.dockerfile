FROM rockylinux:8

RUN yum update -y && \
    yum install -y epel-release && \
    yum update -y && \
    yum --enablerepo epel groupinstall -y "Development Tools" && \
    yum --enablerepo epel install -y findutils gcc gcc-c++ gcc-gfortran \
      git gnupg2 hostname make patch python3 python3-pip unzip wget && \
    yum -y clean all && \
    rm -rf /var/cache

ARG SPACK_VERSION=v0.21.0
RUN git clone --depth=1 --branch=${SPACK_VERSION} https://github.com/spack/spack.git /opt/spack
LABEL SPACK_VERSION=${SPACK_VERSION}
LABEL OS_VERSION="rockylinux:8"

# AST-1508: Prevent parallel builds of cfitsio, since they sometimes fail.
RUN sed -i "16i\    parallel = False" /opt/spack/var/spack/repos/builtin/packages/cfitsio/package.py

# Configure Spack compiler.
RUN . /opt/spack/share/spack/setup-env.sh && spack compiler find
