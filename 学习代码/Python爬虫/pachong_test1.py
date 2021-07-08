from urllib import request

# url = 'http://www.baidu.com'
# response = request.urlopen(url,timeout=1) # timeout 设置网页超时的时间，单位是秒
# print(response.read().decode('utf-8'))

response = request.urlopen('http://www.baidu.com')

# response 的值是一个对象，需要用 read() 读取出来
html = response.read()

# 增加解码的操作
html = html.decode("utf-8")

print(html)

