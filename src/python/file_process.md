## Prelude
```python
import os
import shutil
import sys
```

### 创建文件夹 
create directory
```python
os.mkdir(path, mode=0o777, *, dir_fd=None)
@ path 可以是绝对路径也可以是相对路径
@ dir_fd 是一个文件描述符，通常不用
! 如果path已经存在，该方法会报错

os.makedirs(name, mode=0o777, exist_ok=False)
@ name 文件夹路径
@ exist_ok 设置为True时，允许已经存在的文件夹
```

### 当前文件夹
current directory
```python
os.getcwd()
cwd means current working directory
```

### 删除文件夹
delete directory
```python
os.rmdir(path, *, dir_fd=None)
! 如果path不存在或者非空，该方法会报错

os.removedirs(name)
: 递归删除name里的所有文件夹直到某一个非空的文件夹

shutil.rmtree(dir_path)
: 删除dir_path，无论该路径下面是否有其余文件或文件夹
```

