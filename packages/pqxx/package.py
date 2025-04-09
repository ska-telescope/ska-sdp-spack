from spack.package import *


class Pqxx(CMakePackage):
    """libpqxx is the official C++ client API for PostgreSQL, the
    enterprise-strength open-source relational database. (If "PostgreSQL" is
            too verbose, call it by its shorter name, postgres)."""

    homepage = "https://pqxx.org/development/libpqxx/"
    git      = "https://github.com/jtv/libpqxx.git"

    version('7.7.4', commit='17e5a6c8ac3abc05329891aaa378bd6004b9c8ee')
    version('6.4.8', commit='d631e84b2f0ecad3f0d9237168ad6100abfbd5b9')

    depends_on('cmake@:3.29.6', type='build')

    #
    # these versions are not recommended:
    #

    #version('6.3.0', commit='d6ffb1a13e76995253ef698fb8a6b3d4c6499179')
    # it provides no include/pqxx/config-public-compiler.h

    #version('6.2.5', commit='cb6d840200c0f94bae2616baf6dd4652e272f75e')
    # fails on "make install"

    depends_on('python')
    depends_on('postgresql')
