# 方法1

# 定义一个长度为5的int列表
arr = [1, 2, 3, 4, 5]

# 调用列表的__iter__方法， 可通过dir(arr)查看方法列表；
obj = arr.__iter__()

# 获取下一个元素
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
