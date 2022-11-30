import os
import sys
import shutil

currpath = os.getcwd()
newpath = os.path.join(currpath, "./test1")
print(newpath)
# os.makedirs(newpath, exist_ok=True)
# os.removedirs(newpath)
# shutil.rmtree(newpath)
