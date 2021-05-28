import time
#
# print(time.time())  # 从 1970 年到现在经过的秒数
# print(time.localtime()) # 得到当前的年月日时间
#
# # 格式化输出年月日
#
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(time.strftime('%Y-%m-%d %H:%m:%s'))
#
# print(time.strftime('%Y%m%d'))  # 假设将年月日作为文件的名称，且去掉中间的连接符

# datatime 模块，用来作日期的运算

import datetime

nowtime = datetime.datetime.now()  # 返回当前的时间
print(nowtime)
newtime = datetime.timedelta(minutes=10)  # 10 分钟
print(nowtime + newtime)  # 当前时间加上 10 分钟


# 计算某个时间点加上 10 天后的日期

one_day = datetime.datetime(2021,5,27)
add_day = datetime.timedelta(days=10)
print(one_day + add_day)  # 输出 10 天后的日期
