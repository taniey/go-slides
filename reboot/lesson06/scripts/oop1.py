
'''程序猿
'''
class Programmer(object):

    def __init__(self, sex, age, height):
        self.sex = sex
        self.age = age
        self.height = height


class FrontDeveloper(Programmer):
    pass


class EndDeveloper(Programmer):

    def bestLangage(self):
        pass

class PythonDeveloper(Programmer):

    def bestLangage(self):
        print('python')


class GoDeveloper(Programmer):

    def bestLangage(self):
        print('go')


class NodejsDeveloper(Programmer):

    def bestLangage(self):
        print('nodejs')


developer = EndDeveloper('male', 20, 180)
print(developer)