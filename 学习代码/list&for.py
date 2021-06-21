# 从 1 到 10 所有偶然的平方
alist = []
for i in range(1,11) :
		if( i % 2 == 0) :
			alist.append( i*i)   # 这一行需要缩进，不然程序会报错

print(alist)

# 上面的写法在 Python 中还是不够优雅，我们可以使用推导式来简化上面的写法，用列表推导式来代替 for…if 的写法

blist= [i*i for i in range(1,11) if(i % 2 ==0)]
print(blist)

# 改写上一节课定义的字典的写法

zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
             u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')   # 字符串最前面的 u 是 unicode 的缩写，标志星座，不要出现乱码；为了阅读方便，进行换行

z_num = {}
for i in zodiac_name :
    z_num[i] = 0

# 用字典推导式来定义字典

z_num = {i:0 for i in zodiac_name}

