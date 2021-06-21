# 读取人物名称

f = open('name1.txt')
data = f.read()
print(data.split('|'))  # 人名用竖线作为分割

# 读取兵器名称

f2 = open('weapon.txt')
# data2 = f2.read()
i = 1
for line in f2.readlines() :
    if i % 2 == 1 :   # 打印奇数行的内容
        print(line.strip('\n'))  # 奇数行的内容末尾带有换行符 \n，需要用 strip() 来对其进行精简
    i += 1

f3 = open('sanguo.txt')
print(f3.read().replace('\n',''))

# 定义一个简单的函数

# def func(filename):
# 		print(open(filename).read())
#
# func('name1.txt')


