# import request from urllib # 错误的写法

from urllib import request

response = request.urlopen('http://placekitten.com/g/500/600')
cat_image = response.read()

# 图片也是文件，也是由二进制数据组成的，我们把接收到的二进制数据写入 jpg 格式的文件
with open('cat_500_600.jpg','wb') as f:
    f.write(cat_image)
