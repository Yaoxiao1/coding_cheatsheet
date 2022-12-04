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

### 复制文件夹
copy directory
```python
shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2,ignore_dangling_symlinks=False, dirs_exist_ok=False)
: 完整复制整个src文件夹到dst
@ symlinks 如果为True, 所有src中的软链接都是复制软链接而不是指向的文件
```
### 判断是文件/文件夹
determine file/directory
```python
os.path.isfile(path)
: 判断是文件
os.path.isdir(path)
: 判断是文件夹
```
### 判断文件存在
determine exists
```python
os.path.exists(path)
```
### 复制文件
delete/copy file
``` python
shutil.copy(src, dst, *, follow_symlinks=True)
@ src 文件源地址
@ dst 文件目标地址，可以是文件，也可以是文件夹，如果是文件夹，就在该文件夹里创造同名文件
@ follow_symlinks 当src是一个symbolic link软连接时。如果设为false, dst也是一个软连接；设置为true时，新文件是src指向的文件的复制
: dst文件的创建时间是copy的时间而不是src的时间

shutil.copy2(src, dst, *, follow_symlinks=True)
: 参数跟copy完全相同，唯一的区别是dst会保留元数据，也就是文件创建时间、修改时间等跟源文件是一样的，

shutil.copyfile(src, dst, *, follow_symlinks=True)
: dst必须是文件路径，当src跟dst相同时报SameFileError
```
### 删除文件
delete file
``` python
os.remove(path, *, dir_fd=None)
: 删除path指向的文件，如果path不存在，抛出FileNotFoundError
! Windows系统中如果path文件正在使用也会抛出错误
```

### 列出文件夹里的文件
list directory
``` python
os.listdir(path='.')
```

### 合并路径
join path
``` python
os.path.join(path, *paths)
```