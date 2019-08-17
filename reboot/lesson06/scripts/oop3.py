
'''程序猿
'''
class Programmer(object):

    # 局部变量， 所有方法均可以直接访问，无需实例化.
    monkey = 'Play Computer'

    # 构造函数
    def __init__(self, name, age, height):
        self.name = name        # 可以公开访问
        self._age = age         # 类的私有属性，是编程规范的约束而非Python语法的越苏
        self.__height = height  # 对外伪私有属性

    # 方法
    def get_height(self):
        return self.__height

    @classmethod
    def get_monkey(cls):
        return cls.monkey

    @property
    def get_age(self):
        return self._age

    def get_introduction(self):
        return "My name is {}, I am {} year olds".format(self.name, self._age)



# 对象 = 类的实例化
programmer = Programmer('monkey', 12, 180)
for i in dir(programmer):
    print(i)
print("--------------")
print(Programmer.get_monkey())
print("--------------")
print(programmer.get_age)
print("--------------")
print(programmer.get_introduction())