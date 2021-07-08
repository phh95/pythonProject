import requests

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text

from bs4 import BeautifulSoup

# 第二个参数，是解析 demo 的解释器，对 demo 进行 html 的解析
soup = BeautifulSoup(demo, "html.parser")
# 此时的 soup 变量就代表了解析后的 html 页面

# 打印页面的 title 标签，是浏览器标签页的名称
print(soup.title)

# 获取页面的超链接标签 a
tag = soup.a
print(tag)

# 获得 a 标签的名字
print(soup.a.name)

# 获得 a 标签的父亲的名字，即包含 a 标签的上一层标签
print(soup.a.parent.name)

# 上面的代码返回 p 标签，我们查看 p 标签的上一层标签
print(soup.a.parent.parent.name)

# 获得标签的属性
print(tag.attrs)

# 由于属性返回的是字典，我们还可以对其使用字典的操作
print(tag.attrs['class'])

# 查看标签属性的类型，是一个字典类型
print(type(tag.attrs))






# 打印出来
# print(soup.prettify())