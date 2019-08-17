
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




class BackendProgrammer(Programmer):

    def __init__(self, name, age, height, phone):
        super(BackendProgrammer, self).__init__(name, age, height)
        self.phone = phone



# 对象 = 类的实例化
programmer = BackendProgrammer('monkey', 12, 180, '132xxx')
print(dir(programmer))
print(isinstance(programmer, Programmer))