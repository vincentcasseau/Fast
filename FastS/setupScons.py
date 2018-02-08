#!/usr/bin/env python
from distutils.core import setup, Extension
import os, sys

#=============================================================================
# FastS requires:
# ELSAPROD variable defined in environment
# C++ compiler
# Fortran compiler: defined in config.py
# Numpy
# KCore
#=============================================================================

# Write setup.cfg file
import KCore.Dist as Dist
Dist.writeSetupCfg()

# Test if numpy exists =======================================================
(numpyVersion, numpyIncDir, numpyLibDir) = Dist.checkNumpy()

# Test if kcore exists =======================================================
(kcoreVersion, kcoreIncDir, kcoreLibDir) = Dist.checkKCore()

from KCore.config import *

# Compilation des fortrans ====================================================
prod = os.getenv("ELSAPROD")
if prod is None: prod = 'xx'

# Setting libraryDirs, include dirs and libraries =============================
libraryDirs = ["build/"+prod, kcoreLibDir, '.']
includeDirs = [numpyIncDir, kcoreIncDir]
libraries = ["fastS1", "fastS2", "fastS3", "fastS4", "fastS1", "fastS2", "fastS3", "fastS4", "kcore"]
(ok, libs, paths) = Dist.checkFortranLibs([], additionalLibPaths)
libraryDirs += paths; libraries += libs
(ok, libs, paths) = Dist.checkCppLibs([], additionalLibPaths)
libraryDirs += paths; libraries += libs
 
##   
## Modif pour calcul MPI sur poste GC   
##   
#libraryDirs += ["/usr/lib64/openmpi/lib"]
#libraries += ['mpi_f77'] 

# Extensions ==================================================================
listExtensions = []
listExtensions.append(
    Extension('FastS.fasts',
              sources=['FastS/fastS.cpp'],
              include_dirs=["FastS"]+additionalIncludePaths+includeDirs,
              library_dirs=additionalLibPaths+libraryDirs,
              libraries=libraries+additionalLibs,
              extra_compile_args=Dist.getCppArgs(),
              extra_link_args=Dist.getLinkArgs()+['-p']
              ) )
    
# setup ======================================================================
setup(
    name="FastS",
    version="2.6",
    description="Fast for structured grids.",
    author="Onera",
    package_dir={"":"."},
    packages=['FastS'],
    ext_modules=listExtensions
    )

# Check PYTHONPATH ===========================================================
Dist.checkPythonPath(); Dist.checkLdLibraryPath()
