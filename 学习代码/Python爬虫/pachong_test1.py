from urllib import request

url = 'http://www.baidu.com'
response = request.urlopen(url,timeout=1) # timeout 设置网页超时的时间，单位是秒
print(response.read().decode('utf-8'))
