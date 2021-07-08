# 向百度、360 提交关键词

import requests
#
# kv = {'wd': 'Python'}
#
# r = requests.get("http://www.baidu.com/s", params = kv)
# print(r.status_code)
#
# # 查看我们发给百度的 request 对应的 url 是什么
# print(r.request.url)
#
# print(len(r.text))


# 全代码

keyword = 'Python'
try:
    kv1 = {'user-agent': 'Mozilla/5.0'}
    kv = {'wd': keyword}
    r = requesrts.get("http://www.baidu.com/s", headers = kv1 , params = kv)
    print(r.request.url)
except:
    print("爬取失败")




