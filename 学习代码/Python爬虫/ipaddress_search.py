import requests

url = "https://www.ip138.com/iplookup.asp?ip="
kv = {'user-agent': 'Mozilla/5.0'} # 不添加 user-agent，返回的状态码为 404

r = requests.get(url + "121.8.171.52",headers = kv)
print(r.status_code)

# 返回文本的最后 500 个字节
print(r.text[-500:])

# 实践走不通

# IP 地址查询全代码
import requests
url = "https://www.ip138.com/iplookup.asp?ip="
try:
    r = requests.get(url+'202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")
