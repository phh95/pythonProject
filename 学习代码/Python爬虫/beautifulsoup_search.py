import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text

soup = BeautifulSoup(demo, "html.parser")

# 检索 a 标签，返回的结果是一个列表
# print(soup.find_all('a'))
#
# # 同时查找 a 标签和 b 标签，使用列表作为参数
# print(soup.find_all(['a','b']))

# 如果 name 参数的值为 True，就会显示 soup 中的所有标签
# print(soup.find_all(True))

# for tag in soup.find_all(True):
#     print(tag.name)

# 查找所有以 b 开头的标签，需要用到正则表达式

# import re
# for tag in soup.find_all(re.compile('b')):
#     print(tag.name)

# 查找属性值为 course 的 p 标签
# print(soup.find_all('p','course'))

# 以键值对的形式进行查找
# print(soup.find_all(id = 'link1'))

# 查找 id = link 开头的元素
# import re
# print(soup.find_all(id = re.compile("link")))

# find_all 的第三个参数 recursive，默认为 True
# print(soup.find_all('a'))
#
# print(soup.find_all('a', recursive= False))

# find_all 的第四个参数 string
# print(soup)
# print(soup.find_all(string = 'Basic Python'))

# 找出页面中包含 python 字符串的所有文本
import re
print(soup.find_all(string = re.compile('python')))

print(soup.find_all(string = re.compile('Python')))








