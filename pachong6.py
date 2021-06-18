html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'lxml')  # 导入之后，用 lxml 格式来解析 HTML

# 对 HTML 源代码进行美化，即格式化处理
print(soup.prettify())

# 找到 title 标签
print(soup.title)

# 返回 title 标签里的内容
print(soup.title.string)

# 找到 p 标签
print(soup.p)

# 找到 p 标签 class 的名字
print(soup.p['class'])

# 找到第一个 a 标签
print(soup.a)

# 找到所有的 a 标签
print(soup.find_all('a'))

# 找到 id = link3 的标签
print(soup.find(id='link3'))

# 找到文档中的所有文本内容
print(soup.get_text())
