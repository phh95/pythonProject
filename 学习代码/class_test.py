# user1 = {'name': 'tom', 'hp': 100}
# user2 = {'name': 'jerry', 'hp': 80}
#
#
# def print_role(rolename):
#     print('name is %s ,hp is %s' % (rolename['name'], rolename['hp']))
#
#
# print_role(user1)
#
#
# class Player():


# 类增加属性和方法


# class Player():
#     def __init__(self, name, hp, occu):
#         self.name = name
#         self.hp = hp
#         self.occu = occu  # 类增加了一个属性「玩家的职业」
#
#     def print_role(self):   # 定义一个方法
#         print('%s: %s %s' % (self.name, self.hp, self.occu))
#
#     def updateName(self, newname):
#         self.name = newname
#
#
# class Monster():
#     '定义一个新的类'
#     pass  # 使用 pass 表示暂时不运行这个类
#
#
# user1 = Player('tom', 100, 'war')  # tom 的职业是战士
# user2 = Player('jerry', 80, 'master')  # jerry 的职业是法师
#
# user1.print_role()
# user1.updateName('angola')
# user1.print_role()


# class Player():
#     def __init__(self, name, hp, occu):
#         self.__name = name  # 加了下划线之后，变量就不会被实例访问
#         self.hp = hp
#         self.occu = occu  # 类增加了一个属性「玩家的职业」
#
#     def print_role(self):
#         print('%s: %s %s' % (self.__name, self.hp, self.occu))
#
#     def updateName(self, newname):
#         self.name = newname
#
#
# class Monster():
#     '定义一个新的类'
#     pass  # 使用 pass 表示暂时不运行这个类
#
#
# user1 = Player('tom', 100, 'war')  # tom 的职业是战士
# user2 = Player('jerry', 80, 'master')  # jerry 的职业是法师
#
# user1.print_role()
# user1.updateName('angola')  # 这回就不能更改名字了
# user1.print_role()
# user1.name = 'aaaa'
# user1.print_role()

# 类的继承，父类和子类

class Monster():
    def __init__(self,hp=100):
        self.hp = hp
    def run(self):
        print('移动到某个位置')
    def whoami(self):
        print('我是怪物父类')

class Animals(Monster):    # 这是一个子类
    '普通怪物'
    def __init__(self,hp=10):
        super().__init__(hp)

class Boss(Monster):
    'Boss级怪物'
    def __init__(self,hp=1000):
        super().__init__(hp)
    def whoami(self):
        print('我是怪物我怕谁')


a1 = Monster(200)
print(a1.hp)
print(a1.run())

a2 = Animals(5)
print(a2.hp)
print(a2.run())

a3 = Boss(800)
a3.whoami()







