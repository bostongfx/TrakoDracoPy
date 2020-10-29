import setuptools
import os
import sys

import versioneer

from skbuild import setup
# from skbuild.constants import CMAKE_INSTALL_DIR, skbuild_plat_name
# from packaging.version import LegacyVersion
# from skbuild.exceptions import SKBuildError
# from skbuild.cmaker import get_cmake_version

# Add CMake as a build requirement if cmake is not installed or is too low a version
setup_requires = []
# try:
#     cmake_version = LegacyVersion(get_cmake_version())
#     if cmake_version < LegacyVersion("3.5") or cmake_version >= LegacyVersion("3.15"):
#         setup_requires.append('cmake<3.15')
# except SKBuildError:
#     setup_requires.append('cmake<3.15')

# If you want to re-build the cython cpp file (DracoPy.cpp), run:
# cython --cplus -3 -I./_skbuild/linux-x86_64-3.7/cmake-install/include/draco/ ./src/TrakoDracoPy.pyx
# Replace "linux-x86_64-3.6" with the directory under _skbuild in your system
# Draco must already be built/setup.py already be run before running the above command

# C:\P\TrakoDracoPy-venv\Scripts\cython.exe --cplus -3 ^
# --no-docstrings C:/P/TrakoDracoPy/TrakoDracoPy/_TrakoDracoPy.pyx ^
# --output-file C:/P/TrakoDracoPy/_skbuild/win-amd64-3.8/cmake-build/TrakoDracoPy/_TrakoDracoPy.cxx"

# src_dir = './src'
# lib_dir = os.path.abspath(os.path.join(CMAKE_INSTALL_DIR(), 'lib/'))
# cmake_args = []
# if sys.platform == 'darwin':
#     plat_name = skbuild_plat_name()
#     sep = [pos for pos, char in enumerate(plat_name) if char == '-']
#     assert len(sep) == 2
#     cmake_args = ['-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING='+plat_name[sep[0]+1:sep[1]],'-DCMAKE_OSX_ARCHITECTURES:STRING='+plat_name[sep[1]+1:]]
#     library_link_args = ['-l{0}'.format(lib) for lib in ('dracoenc', 'draco', 'dracodec')]
# else:
#     library_link_args = ['-l:{0}'.format(lib) for lib in ('libdracoenc.a', 'libdraco.a', 'libdracodec.a')]
# extra_link_args = ['-L{0}'.format(lib_dir)] + library_link_args

def exclude_draco_sdk(cmake_manifest):
    return list(filter(lambda name: not (
        name.endswith('.a')
        or name.endswith('.lib')
        or name.endswith('.h')
        or name.endswith('.exe')
        or name.endswith('.cmake')
        ), cmake_manifest))

setup(
    name='TrakoDracoPy',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description = 'Python wrapper for Google\'s Draco Mesh Compression Library with Trako support',
    author = 'Manuel Castro, Daniel Haehn',
    author_email = 'macastro@princeton.edu, haehn@mpsych.org',
    url = 'https://github.com/haehn/TrakoDracoPy',
    cmake_process_manifest_hook=exclude_draco_sdk,
    packages=['TrakoDracoPy'],
    setup_requires=setup_requires,
    install_requires=['pytest'],
)
