# Installation de libfast pour etre accessible par les autres modules
# Si libfast.a existe, on la recopie
# Sinon, on cherche fast.so ou fast.pyd, on le recopie en libfast.so ou dll
import os, shutil
import platform
system = platform.uname()[0]

if system == 'Windows':
    __EXTMODULE__ = '.pyd'
    __EXTSHARED__ = '.dll'
else:
    __EXTMODULE__ = '.so'
    __EXTSHARED__ = '.so'

import KCore.installPath as K
libPath = K.libPath
installPathLocal = K.installPath

# La librarie statique existe?
a = os.access(installPathLocal+"/FastC/libfastc.a", os.F_OK)
if a:
    shutil.copyfile(installPathLocal+"/FastC/libfastc.a", libPath+"/libfastc.a")
else: # Essai en dynamique
    a = os.access(installPathLocal+"/FastC/fastc"+__EXTMODULE__, os.F_OK)
    if a:
        shutil.copyfile(installPathLocal+"/FastC/fastc"+__EXTMODULE__,
                        libPath+"/libfastc"+__EXTSHARED__) 
    else:
        print("Error: fastc" +__EXTMODULE__+" can not be found.")