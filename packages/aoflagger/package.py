from spack.package import *


class Aoflagger(CMakePackage):
    """RFI detector and quality analysis
    for astronomical radio observations."""

    homepage = "https://sourceforge.net/projects/aoflagger/"
    git      = "https://gitlab.com/aroffringa/aoflagger.git"
    version('3.1.0', commit='v3.1.0', submodules=True)
    version('3.2.0', commit='v3.2.0', submodules=True)
    version('3.3.0', commit='v3.3.0', submodules=True)
    version('3.4.0', commit='v3.4.0', submodules=True)
    version('latest', branch='master', submodules=True)


    variant('debug-information', default=False, description='Enable debug information')
    variant('gui', default=False, description='Build rfigui and aoqplot tools')

    depends_on('casacore+data')
    depends_on('cfitsio')
    depends_on('fftw')
    depends_on('boost+python+numpy+date_time')
    depends_on('hdf5')
    depends_on('libxml2')
    depends_on('lapack')
    depends_on('lua')
    depends_on('cairo')
    depends_on('git')
    depends_on('python')

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define('ENABLE_GUI', '+gui' in spec),
        ]
        if '+debug-information' in spec:
            args.append(self.define('CMAKE_CXX_FLAGS', "-g"))
        return args
