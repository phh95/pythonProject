# 使用第三方库 requests 来代替 urllib 库

# get 请求
import requests  # 导入 request 库
url = 'http://httpbin.org/get'
data = {'key':'value', 'abc':'xyz'}
# .get 是使用 get 方式请求 url，字典类型的 data 不用进行额外处理
response = requests.get(url,data)
# 返回的时候也不需要管编码的问题，直接使用 .text 方法
print(response.text)


# post 请求
import requests
url = 'http://httpbin.org/post'
data = {'key':'value', 'abc':'xyz'}
response2 = requests.post(url,data)
# 返回类型为 json 格式
print(response2.json())
