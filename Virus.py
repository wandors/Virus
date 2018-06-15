# -*- coding: utf-8 -*-
from re import sub

__author__ = 'Сер.гей Полунец'
import os
import sys
import psutil
import string
import subprocess
import win32file


class Main:
    def __init__(self):
        self. list_disk = []
        self.list_leter = psutil.disk_partitions()
        for i in self.list_leter:
            if i.opts == 'rw,removable':
                self.list_disk.append(i.device)
        if self.list_disk.__len__() > 0:
            for i in self.list_disk:
                for d_f in os.listdir(i):
                    self.files = i + d_f
                    print(self.files)
                    win32file.SetFileAttributes(self.files, win32file.FILE_ATTRIBUTE_NORMAL)
        else:
            pass



if __name__ == '__main__':
    Main()
    input()

