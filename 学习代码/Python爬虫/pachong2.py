from urllib import parse  # parse 模块用来处理 post 请求的数据
from urllib import request

data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf8') # urllib 要去封装我们的数据，定义一个名为 data 的变量

response = request.urlopen('http://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))

response2 = request.urlopen('http://httpbin.org/get', timeout=1)
print(response2.read())
