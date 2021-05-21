# 记录生肖，根据年份来判断生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# print(chinese_zodiac[0])

# print(chinese_zodiac[0:4])

# print(chinese_zodiac[-1])

year = 2018  # 2018 年是狗年
print(year % 12)  # 运行结果为 2，即对应的下标为 2，2 对应序列中的第三个字符
print(chinese_zodiac[year % 12])
