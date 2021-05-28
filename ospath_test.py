import os

print(os.path.abspath('.'))  # 根据相对路径的点 . 获取绝对路径
print(os.path.abspath('..'))  # 获取上一级路径的位置

# 可以使用 os 来判断目录下某个文件是否存在

print(os.path.exists('/Users'))  # 判断根目录下的 users 文件是否存在

print(os.path.isfile('/Users'))  # 判断 users 文件夹是否为一个文件

print(os.path.isdir('/Users'))  # 判断 users 文件夹是否为一个目录


# pathlib 库

from pathlib import Path

p = Path('.')  # 需要先对 . 进行封装
print(p.resolve()) # 打印相对路径对应的绝对路径

# 判断某个文件是否为一个目录

p.is_dir()