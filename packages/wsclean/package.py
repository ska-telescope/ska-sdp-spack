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
    version('latest', branch='master', submodules=True)

    depends_on('hdf5-autotools+cxx@1.10.7')
    depends_on('fftw@3.3.9')
    depends_on('casacore@3.3.0')
    depends_on('everybeam@0.2.0', when='@3.0')
    depends_on('everybeam@latest', when='@latest')
    depends_on('idg+cuda+python@latest')
    depends_on('boost@1.73.0:')
    depends_on('openblas threads=pthreads', when='@latest')

    def setup_build_environment(self, env):
        if self.spec.satisfies('@latest'):
            env.set("OPENBLAS_NUM_THREADS", "1")
