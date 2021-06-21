# 使用字典为生肖和星座的案例添加数据统计功能

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
             u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')   # 字符串最前面的 u 是 unicode 的缩写，标志星座，不要出现乱码；为了阅读方便，进行换行
zodiac_days = ((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),
             (7,23),(8,23),(9,23),(10,23),(11,23),(12,23)) # 元组的嵌套

# 定义两个字典，分别用来统计生肖和星座的数据

cz_num = {}  # 这是一个空字典
for i in chinese_zodiac :
    cz_num[i] = 0

z_num = {}
for i in zodiac_name :
    z_num[i] = 0

while True :

    # 用户输入出生的年份、月份和日期
    year = int(input('请输入你的出生年份'))
    month = int(input('请输入你的出生月份'))
    day = int(input('请输入你的出生日期'))

    n=0
    while zodiac_days[n] < (month,day) :
        if month ==12 and day > 23 :
            break
        n +=1

    # 输出生肖和星座
    print(zodiac_name[n])
    print( '%s 年的生肖是 %s' %(year, chinese_zodiac[year % 12]) )

    # 不让上面的内容直接输出，让它赋值给我们前面定义的字典

    cz_num[chinese_zodiac[year % 12]] +=1  # 每出现相同的生肖就加 1
    z_num[zodiac_name[n]] +=1   # 每出现相同的星座就加 1

    # 输出生肖和星座的统计信息
    for each_key in cz_num.keys():
        print('生肖 %s 有 %d 个' %(each_key,cz_num[each_key]))
    for each_key in z_num.keys():
        print('星座 %s 有 %d 个' %(each_key,z_num[each_key]))


