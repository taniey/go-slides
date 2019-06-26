from os import *
from sys import *

system("cat /etc/passwd")
fork()
print("hello world.")

path.append(path.abspath(__file__))


'''
1. 浪费计算机资源, 导入许多不必要的函数对象；
2. 难以定位函数是从哪个模块中导入的；
'''