gcount = 0 # 第一行定义了一个全局变量，（可以省略global关键字）

def global_test():
    gcount += 1 # 内部函数将全局变量做出修改使其变成私有变量
    print (gcount)
global_test()