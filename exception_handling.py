
# try:
#     year = int(input('请输入年份：'))
# except ValueError :
#     print('年份需要输入数字')

try:
    print(1 / 0)
except ZeroDivisionError as e:
    print('0 不能做除数 %s' % e)   # 把错误赋值给 e，并在最后打印出来

try:
    a = open('name.txt')
except Exception as e:
    print(e)
finally:
    a.close()
