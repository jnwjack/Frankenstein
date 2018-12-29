import sys
from cx_Freeze import setup, Executable

includefiles = [""]

base = None
if(sys.platform == "win64"):
    base = "Win64GUI"
if(sys.platform == "win32"):
    base = "Win32GUI"
setup(
    name = "Frankenstein.pyw" ,
    version = "0.1" ,
    description = "2015 Jack Wohl" ,
    #options = {"build_exe": build_options},
    executables = [Executable("Frankenstein.pyw",base=base)] ,
)
