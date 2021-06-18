# 配合正则表达式抓取网页图片链接和名称

import requests
import re
content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text
print(content)


# HTML 中我们要抓取的内容
# <div class ="grid-item work-thumbnail">
# <a href = "http://www.cnu.cc/works/526000" class ="thumbnail" target="_blank">
# <div class ="title">沉沦</div>
# <div class ="author">壹飛哥哥</div>

pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)
results = re.findall(pattern, content)
print(results)

for result in results:
    url,name = result
    print(url,re.sub('\s','',name))



