from spack.package import *


class PqxxAutotools(AutotoolsPackage):
    """libpqxx is the official C++ client API for PostgreSQL, the
    enterprise-strength open-source relational database. (If "PostgreSQL" is
            too verbose, call it by its shorter name, postgres)."""

    homepage = "https://pqxx.org/development/libpqxx/"
    git      = "https://github.com/jtv/libpqxx.git"

    version('5.1.1', commit='ae16ffc87c7eeec8fa936ca1c75c5660761be619')
    version('5.0.1', commit='0e93d8ebf542a298dfbd4afdc419113b246a093a')

    variant("doc", default=False, description="Build documentation")

    depends_on('postgresql')
    depends_on('python')
    depends_on('doxygen')
    depends_on('xmlto')

    def install(self, spec, prefix):
        configure("--prefix=" + prefix)
        make()
        make("install")

    # the configure arguments seem to be ignored
    def configure_args(self):
        spec = self.spec
        args = []
        if ('+doc') in spec:
            args.append("--enable-documentation")
        else:
            args.append("--disable-documentation")
        args.append("--enable-shared")
        return args

    parallel = False
