# 迭代器

# 创建一个步长为小数的迭代器

# def float_range(start, stop, step):
#     x = start
#     while x < stop:
#         yield x
#         x += step
#
#
# for i in float_range(10, 20, 0.5):
#     print(i)


# 定义函数

# def describe_pet(animal_type, pet_name):
#     """显示宠物的信息"""  # 描述
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
# describe_pet('dog', 'donggua')

# 形参默认值

# def describe_pet(pet_name, animal_type='dog'):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
# describe_pet(pet_name='wille')

# return 语句

# def get_formatted_name(first_name,last_name):
# 	"""返回包含姓氏和名字的全名"""
# 	full_name = f'{first_name} {last_name}'  # first_name 和 last_name 中间有一个空格
# 	return full_name.title()  # 返回的单词首字母为大写
#
# my_fullname = get_formatted_name('honghao','peng') # 调用函数，要把返回的值赋值给一个变量
# print(my_fullname)


# 让实参变成可选的

# def get_formatted_name(first_name,last_name,middle_name=''):
# 	if middle_name != '':  # middle_name 不为空值时
# 		full_name = f'{first_name} {middle_name} {last_name}'
# 	else:   # middle_name 为空值时
# 		full_name = f'{first_name} {last_name}'
# 	return full_name.title()
#
# my_fullname = get_formatted_name('jimi','hendrix')
# print(my_fullname)
#
# my_fullname = get_formatted_name('john','hooker','lee')
# print(my_fullname)

# 返回字典
# 我们最终想返回的字典为 {'first':'jimi','last':'hendrix'}

# def build_person(first_name,last_name):
# 	person = {'first':first_name,'last':last_name}
# 	return person
#
# my_fullname = build_person('jimi','hendrix')
# print(my_fullname)

# 给返回的字典增加一个键值对

# def build_person(first_name,last_name,age=None):  # 将 None 视为占位值
# 	person = {'first':first_name,'last':last_name}
# 	if age:
# 		person['age']=age
# 	return person
#
# my_fullname = build_person('jimi','hendrix',age=27)
# print(my_fullname)

# 可变长参数，即传递任意数量的实参

# def make_pizza(*toppings):
# 	print(toppings)
#
# make_pizza('tomatoes')
# make_pizza('tomatoes','mushrooms','cheese')


# 结合使用位置实参和可变长参数

# def make_pizza(size,*toppings):
# 	print(f"\nMaking a {size}-inch pizza with the following toppings:")
# 	for topping in toppings:
# 		print(f"- {topping}")
#
# make_pizza(12,'tomatoes','mushrooms','cheese')

# 使用任意数量的关键字实参

def build_profile(first,last,**user_info):
    user_info['first_name']= first
    user_info['last_name']= last
    return user_info

user_profile = build_profile('albert','einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
















