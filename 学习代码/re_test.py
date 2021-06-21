# 正则表达式库 re

import re

# p = re.compile('a')
# print(p.match('a'))  # match 里面放被匹配的字符串


# p = re.compile('ca*t')
# print(p.match('caaaaat'))

# 正则表达式分组功能实例

# p = re.compile(r'(\d+)-(\d+)-(\d+)')  # 字符串最前面加上 r，目的是为了不让字符串进行转义，让它保持原样
# print(p.match('2021-05-25'))
# print(p.match('2021-05-25').group(2))  # group 的值为 2，就是取出月份，如果值为 1，则是取出年份
# print(p.match('2021-05-25').groups())
# year,month,day = p.match('2021-05-25').groups()
# print(year)
# print(month)
# print(day)

# sub 函数

phone = '123-456-789 # 这是电话号码'
# 将末尾的注释去掉
p2 = re.sub(r'#.*$','',phone)
print(p2)
# 去掉电话号码中间的横杆
p3 = re.sub(r'\D','',p2)  # \D 匹配不包含数字的文本
print(p3)