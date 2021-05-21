# def zhihu(func):
#     def wrapper():
# 		print('谢邀')
# 		func()
# 		print('以上')
# 	return wrapper
#
#
# @zhihu
# def answer1():
# 		print('我也不知道')
#
# answer1()


# 不用装饰器的写法如下：

# def zhihu(func):
#     def wrapper():
#         print('谢邀')
#         func()
#         print('以上')
#     return wrapper
#
# def answer1():
#     print('我也不知道')
#
# answer1 = zhihu(answer1)
# answer1()