import requests
import os

url = "http://img0.dili360.com/pic/2021/01/15/60010e2692ab69g26671088_t.jpg"
root = "/Users/penghonghao/PycharmProjects/"
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
# 调用 open() 函数时，传入标识符 'w' 或者 'wb' 表示写文本文件或写二进制文件
# 图片是二进制文件
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")

