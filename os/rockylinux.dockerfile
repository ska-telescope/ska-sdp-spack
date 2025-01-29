FROM rockylinux:8

RUN yum install -y bzip2 file gcc-toolset-10 git patch xz && \
    yum -y clean all && \
    rm -rf /var/cache

ARG SPACK_VERSION=v0.23.0
RUN git clone --depth=1 --branch=${SPACK_VERSION} https://github.com/spack/spack.git /opt/spack
LABEL SPACK_VERSION=${SPACK_VERSION}
LABEL OS_VERSION="rockylinux:8"

# AST-1508: Prevent parallel builds of cfitsio, since they sometimes fail.
RUN sed -i "16i\    parallel = False" /opt/spack/var/spack/repos/builtin/packages/cfitsio/package.py

# Configure Spack compiler.
RUN . /opt/rh/gcc-toolset-10/enable && \
    /opt/spack/bin/spack compiler find && \
    /opt/spack/bin/spack compiler remove gcc@8.5.0
