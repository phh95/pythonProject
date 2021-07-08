import requests

# r = requests.get('https://www.amazon.cn/dp/B0785D5L1H')
# print(r.status_code)
# print(r.encoding)
# # print(r.text)
# print(r.request.headers)  # 返回我们访问服务器的请求头


# kv = {'user-agent':'Mozilla/5.0'}
# url = 'https://www.amazon.cn/dp/B0785D5L1H'
# r = requests.get(url,headers = kv)
# print(r.status_code)
# print(r.request.headers)
# print(r.text[:1000])

# 爬取亚马逊商品页面全代码

import requests

url = "https://www.amazon.cn/dp/B0785D5L1H"
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print('爬取失败')
