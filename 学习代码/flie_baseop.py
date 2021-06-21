# 将小说的主要人物记录在文件中

# file1 = open('name.txt', 'w')  # 第二个参数 'w' 代表的是写入
# file1.write('诸葛亮')
# file1.close()

# 读取 name.txt 文件的内容

# file2 = open('name.txt')
# print(file2.read())
# file2.close()
#
# file3 = open('name.txt', 'a')  # 第二个参数 'a' 代表的是增加
# file3.write('刘备')
# file3.close()

# file4 = open('name.txt')
# print(file4.readline())

# 逐行读取

# file5 = open('name.txt')
# for line in file5.readlines() :
#     print(line)
#     print('=====')    # 为了方便区分，我们在后面多输出一些提示信息

# file6 = open('name.txt')
# print(file6.tell())  # 打印指针所在的位置
# file6.read(1)
# print(file6.tell())
# file6.seek(0)  # 返回到文件的开头
# print(file6.tell())

file6 = open('name.txt')
print('当前文件指针的位置 %s' %file6.tell())
print('当前读取到了一个字符，字符的内容是 %s' %file6.read(1))
print('当前文件指针的位置 %s' %file6.tell())

file6.seek(0)
print('我们进行了 seek 操作')
print('当前文件指针的位置 %s' %file6.tell())
print('当前读取到了一个字符，字符的内容是 %s' %file6.read(1))
print('当前文件指针的位置 %s' %file6.tell())
file6.close()










