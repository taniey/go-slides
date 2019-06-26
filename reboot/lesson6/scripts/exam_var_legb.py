age = 20
def func():
    address = "beijing"
    global age  # global 可以将局部变量提升为全局变量
    age = 30
    print(address)
    print(age)
