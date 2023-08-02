from distutils.core import setup
import py2exe
import os

setup(windows=['RemotePlayAutoHDR.py'])

#copy HDRSwitch.exe to dist folder
os.system("copy HDRSwitch.exe dist\HDRSwitch.exe")
#copy icon.ico to dist folder
os.system("copy icon.ico dist\icon.ico")

#rename dist folder to RemotePlayAutoHDR
os.system("rename dist RemotePlayAutoHDR")