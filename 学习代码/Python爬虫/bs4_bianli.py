import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text

soup = BeautifulSoup(demo, "html.parser")

# # 返回 html 页面的 head 标签，里面包含一个儿子节点 title 标签
# print(soup.head)
#
# # 下行遍历，contents 方法返回的是一个列表
# print(soup.head.contents)
#
# # 查看 body 标签的 contents 信息
# print(soup.body.contents)
#
# # print(soup.body)
#
# # 可以使用 len 获得儿子节点的数量
# print(len(soup.body.contents))
#
# # 获取其中第二个儿子节点的信息，可以使用列表的索引
# print(soup.body.contents[1])

# 上行遍历，查看 title 标签的父亲节点
# print(soup.title.parent)
#
# # 查看 html 标签的父亲节点
# print(soup.html.parent)

# 平行遍历，返回 a 标签的下一个平行标签
# print(soup.a.next_sibling)

print(soup.a.next_sibling.next_sibling)




# print(soup.prettify())

