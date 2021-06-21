# bicycles = ['trek','cannondale','redline','specialized']
#
# # 花括号内的变量替换为其值
#
# message = f"My first bicycle was a {bicycles[0].title()}."   # f字符串
# print(message)

# 为一个空列表添加元素

# motorcycles = []
#
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
#
# print(motorcycles)

# 使用 pop 删除列表中的元素

# motorcycles = ['honda','yamaha','suzuki']
# last_one = motorcycles.pop()  # pop 默认弹出最后一个元素
# print(motorcycles)
# print(last_one)

# 指定弹出列表中任意位置的元素

# motorcycles = ['honda','yamaha','suzuki']
# first_one = motorcycles.pop(0)  # 指定弹出第一个元素
# print(motorcycles)
# print(first_one)

# 按单词首字母进行排序

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)
#
# # 按单词首字母相反的顺序进行排列
#
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
# print(cars)

# # 使用 sorted 进行临时排序
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(sorted(cars))
# print(cars)  # 最后还是恢复为原先的排序

# 倒着打印列表元素

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)






