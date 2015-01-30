# -*- coding: utf-8 -*-
'''
Created on 2015/1/4

@author: sam
'''
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ['lpod',"os","xml","xlrd"],
                     "includes":['lxml.etree', 'lxml._elementpath', 'gzip'],
                     "include_files": [('template.odt','templates'),('namespaces.xml','templates')],
                     "include_msvcr":True,
                     "create_shared_zip": False}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "AdCardMaker",
        version = "0.2",
        description = "Admission card maker",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base)])