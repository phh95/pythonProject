
def counter():
    cnt = [0]
    def add_one():
        cnt[0] += 1
        return cnt[0]

    return add_one


num1 = counter()

# num1 后面有没有加括号，运行的值是不一样的

print(num1)   # 返回的结果是一个函数类型
print(num1())  # 返回一个数字
print(num1())