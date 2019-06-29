
'''程序猿
'''
class Programmer(object):

    # 构造函数
    def __init__(self, name, age):
        self.name = name        # 可以公开访问
        self.age = age

    # 方法
    def __eq__(self, other):
        return self.age == other.age

    # 方法
    def __add__(self, other):
        return self.age + other.age



p1 = Programmer('monkey1', 12)
p2 = Programmer('monkey1', 12)

print(p1 == p2)
print(p1 + p2)