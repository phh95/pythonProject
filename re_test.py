# 正则表达式库 re

import re

# p = re.compile('a')
# print(p.match('a'))  # match 里面放被匹配的字符串


p = re.compile('ca*t')
print(p.match('caaaaat'))
