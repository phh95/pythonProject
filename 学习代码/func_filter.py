# filter 与 lambda 表达式配合使用

# a = [1,2,3,4,5,6,7]
# print(list(filter(lambda x:x>2,a)))

# zip() 函数的例子

# a = (1,2,3)
# b = (4,5,6)
#
# for i in zip(a,b):
#     print(i)

# 闭包

def func():
    a = 1
    b = 2
    return a+b

def sum(a):
    def add(b):
        return a+b
    return add

num1 = func()

num2 = sum(2)

print(type(num1))
print(type(num2))
