# 迭代器

# 创建一个步长为小数的迭代器

def float_range(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


for i in float_range(10, 20, 0.5):
    print(i)
