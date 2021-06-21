class Testwith():
    def __enter__(self):
        print('run')
    def __exit__(self, exc_type, exc_val, exc_tb):  # exc_tb 用来监测异常信息
        if exc_tb is None:
            print('程序运行正常，顺利结束')
        else:
            print('has error %s' %exc_tb)

with Testwith():   # 调用前面定义的类
    print('Test is runing')
    raise NameError('testNameError')   # 手动抛出异常