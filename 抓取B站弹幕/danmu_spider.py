import pprint

import requests
import re

for date in range(9,12):
    url = f'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=338244746&date=2021-06-{date}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91',
        'cookie':''
    }
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8'  # 解决返回的弹幕乱码
    # print(response.text)
    # 正则表达式提取出来的内容是列表
    danmu_list = re.findall(':(.*?)@',response.text)
    for i in danmu_list:
        danmu = i[1:]  # 切片操作
        with open('弹幕.txt', mode='a', encoding='utf-8') as f:
            f.write(danmu)
            f.write('\n')
            print(danmu)
