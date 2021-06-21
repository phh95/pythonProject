# 搜索人名、兵器在《三国演义》中出现的次数，类似于 Word 中的查找功能

import re

def find_item( hero ) :
    with open('sanguo.txt') as f :
        data = f.read().replace('\n','')
        name_num = re.findall(hero,data)   # 引入一个 re 的模块，这里统计的是 hero 在 data 中出现的次数
       # print('主角 %s 出现 %s 次' %(hero,len(name_num)))  # findall 返回的结果不是次数，出现多少次，就会在列表中打印多少次

    return len(name_num)

# 读取人物的信息
name_dict = {}
with open ('name1.txt') as f:    # 打开文件时通过一个变量 f 进行访问
    for line in f:
        names = line.split('|')
        for n in names:
#            print(n)
            name_num = find_item(n)  # 把主角的名字传递给前面定义的函数，返回名字出现的次数
# 为了方便统计次数，这里我们使用一个字典
            name_dict[n] = name_num

# 对出现的次数进行排序，从大到小

name_sorted = sorted(name_dict.items(),key=lambda item: item[1], reverse=True)
print(name_sorted[0:10])