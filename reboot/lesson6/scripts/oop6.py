
'''程序猿
'''
class Programmer(object):

    # 构造函数
    def __init__(self, name, age):
        self.name = name        # 可以公开访问
        self.age = age

    # 方法
    def __str__(self):
        return '{} is {} years old.'.format(self.name, self.age)

    # 方法
    def __dir__(self):
        return self.__dict__.keys()



p1 = Programmer('monkey1', 12)
print(p1)
print(dir(p1))
