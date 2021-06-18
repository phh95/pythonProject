import pprint

import requests
import re

for date in range(9,12):
    url = f'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=338244746&date=2021-06-{date}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91',
        'cookie':'buvid3=D6149864-C1D8-9E9A-1F33-BF7149EB56A607131infoc; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(um||k)Y~RR0J\'uYuJ)))lu|; fingerprint=ec1c09daae8fe3d154ed8157ce5813e3; buvid_fp=D6149864-C1D8-9E9A-1F33-BF7149EB56A607131infoc; buvid_fp_plain=D6149864-C1D8-9E9A-1F33-BF7149EB56A607131infoc; SESSDATA=d1710e35%2C1629440520%2C3fa7d%2A21; bili_jct=3ed189e90fbf5e7c5addc534474da604; DedeUserID=18105372; DedeUserID__ckMd5=5aa1e460dcbdf39e; sid=jcs58175; _uuid=ADA8585C-1A08-829D-7166-67B04843A87510162infoc; LIVE_BUVID=AUTO7216209959077133; bp_t_offset_18105372=534354567972934714; CURRENT_QUALITY=80; bfe_id=018fcd81e698bbc7e0648e86bdc49e09; bp_video_offset_18105372=537674685070454589'
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
