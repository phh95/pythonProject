import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text

soup = BeautifulSoup(demo, "html.parser")

# 检索 a 标签，返回的结果是一个列表
print(soup.find_all('a'))

# 同时查找 a 标签和 b 标签，使用列表作为参数
print(soup.find_all(['a','b']))

# 如果 name 参数的值为 True，就会显示 soup 中的所有标签
# print(soup.find_all(True))

for tag in soup.find_all(True):
    print(tag.name)

# 查找所有以 b 开头的正则表达式

