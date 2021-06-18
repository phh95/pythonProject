from pandas import Series, DataFrame
import pandas as pd  # 另外一种引入的方式

obj = Series([4, 5, 6, -7])

# print(obj)
#
# print(obj.index)
# print(obj.values)


obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'c', 'a'])  # 指定索引index的值

# print(obj2)

obj2['c'] = 6  # 对索引对应的 value 重新赋值
# print(obj2)

# 把字典转换为 Series

sdata = {'beijing': 35000, 'shanghai': 71000, 'guangzhou': 16000, 'shenzhen': 5000}
obj3 = Series(sdata)
# print(obj3)

obj3.index = ['bj', 'sh', 'gz', 'sz']
# print(obj3)


data = {'city': ['shanghai', 'shanghai', 'shanghai', 'beijing', 'beijing'],
        'year': [2020, 2021, 2022, 2023, 2024],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = DataFrame(data)
# print(frame)

frame2 = DataFrame(data, columns=['year', 'city', 'pop'])
# print(frame2)

# 提取出一维数据

# print(frame2.year)
# print(frame2['city'])

frame2['new'] = 100  # 为 DataFrame 增加新的一列 new
print(frame2)

frame2['captial'] = frame2.city == 'beijing'   # 根据 city 是否为北京，生成新的一列
print(frame2)
