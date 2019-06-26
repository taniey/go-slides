# https://www.cnblogs.com/z360519549/p/5172020.html
def outer_v1():
    a = 10
    def inner():
        b= 10
        print(b)
        print(a)
    return inner


f1 = outer_v1()
f1()

def outer_v2():
    a = 10

    def inner():
        nonlocal a  # nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
        b= 10
        print(b)
        a += 1
        print(a)
    return inner

f2 = outer_v2()
f2()