# while 循环中嵌套 if 语句，实现输入日期判断用户的星座

zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
             u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')   # 字符串最前面的 u 是 unicode 的缩写，标志星座，不要出现乱码；为了阅读方便，进行换行

zodiac_days = ((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),
             (7,23),(8,23),(9,23),(10,23),(11,23),(12,23)) # 元组的嵌套

# 用户输入月份和日期
int_month = int(input('请输入你的出生月份'))
int_day = int(input('请输入你的出生日期'))

n = 0
while zodiac_days[n] < (int_month,int_day) :
    if int_month == 12 and int_day > 23 :
        break    # 如果用户输入的日期大于 12 月 23 日，则循环终止，不会运行下面的 n = n+1
    n += 1   # 这个语句等价于 n = n+1
print(zodiac_name[n])