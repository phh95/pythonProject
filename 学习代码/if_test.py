# 分支结构

# 根据输入的分数，进行评级

# score = input('请输入你的分数：')
# score = int(score)  # 把输入的文本转换为整数
#
# if 0 <= score < 60:
#     print('D')
# elif 60 <= score < 80:
#     print('C')
# elif 80 <= score < 90:
#     print('B')
# elif 90 <= score < 100:
#     print('A')
# elif score == 100:
#     print('S')
# else:
#     print('温馨提示：输入的分数有误，请输入 0-100 之间的分值！')
#


# 条件表达式

age = 16
if age < 18:
    print('抱歉，未满18周岁，禁止访问本网站')
else:
    print('欢迎您来')

# 将上面的代码改写成条件表达式的写法

print('抱歉，未满18周岁，禁止访问本网站') if age < 18 else print('欢迎您来')


# 判断两个数的大小，将较小的数赋值给 small

a = 3
b = 5

if a < b:
    small = a
else:
    small = b

# 将上面的写法改写成条件表达式

small = a if a < b else b
print(small)