# 装饰器带了参数，就需要在最外面多嵌套一层

def new_tips(argv):
    def tips(func):   # 装饰器带的参数 add 传递到 argv 里面
        def nei(a,b):
            print('start %s' %argv)
            func(a,b)
            print('stop')

        return nei
    return tips

@new_tips('add')  # 装饰器带了一个字符串参数 add
def add(a,b):
    print(a+b)

print(add(4,5))