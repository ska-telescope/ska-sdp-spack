# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Wsclean(CMakePackage):
    """WSClean (w-stacking clean) is a fast generic widefield imager. It
       implements several gridding algorithms and offers fully-automated multi-scale
       multi-frequency deconvolution."""

    homepage = "https://wsclean.readthedocs.io/"
    git      = "https://gitlab.com/aroffringa/wsclean.git"

    version('3.0', commit='9ee587c576caad779dc127bb3f83858513679333', submodules=True)
    version('3.0.1', commit='1a4e5928689b23d3034549c2541829427d91fa8e', submodules=True)
    version('latest', branch='master', submodules=True, preferred=True)

    depends_on('hdf5+cxx')
    depends_on('fftw')
    depends_on('casacore')
    depends_on('everybeam@0.2.0', when='@3.0')
    depends_on('everybeam@0.3.0', when='@:3.0')
    depends_on('idg+cuda+python')
    depends_on('boost+date_time+program_options')
    depends_on('openblas threads=pthreads')
    depends_on('gsl')

    def setup_build_environment(self, env):
        env.set("OPENBLAS_NUM_THREADS", "1")

    def setup_run_environment(self, env):
        env.set("OPENBLAS_NUM_THREADS", "1")
        spec = self.spec
