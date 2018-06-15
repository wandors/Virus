# -*- coding: utf-8 -*-
__author__ = 'Сергі Полунець'
__versions__ = "v.6.0.2"
import os
names = "Test"
scripts = "Test"
icons = "Exe"
num = 1
if str(num) == "1":
    pacs = "--onefile --console"
elif str(num) == "2":
    pacs = "--windowed"
elif str(num) == "3":
    pacs = "--onefile --windowed"
else:
    pacs = "--console"
os.system("pyinstaller.exe {0} --icon={1}.ico {2}.py --name={3}".format(pacs, icons, scripts, names))
#os.system("del /a " + "{0}.spec".format(names))
