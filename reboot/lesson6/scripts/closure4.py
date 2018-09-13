
stu_time_v1 = 0

'''
    如果一个函数使用了和全局变量相同的名字且改变了该变量的值，那么该变量就会变成局部变量，那么就会造成在函数中我们没有进行定义就引用了，所以会报该错误
'''
def insert_stu_time_v1(min):
    stu_time_v1 = stu_time_v1 + min
    return stu_time_v1

# print(insert_stu_time_v1(2))
# print(insert_stu_time_v1(10))

''''
    如果局部变量想要修改全局变量的值，那么必须用global在局部变量中声明
'''

stu_time_v2 = 1

def insert_stu_time_v2(min):
    global stu_time_v2
    stu_time_v2 = stu_time_v2 + min
    return stu_time_v2

print(insert_stu_time_v2(2))
print(insert_stu_time_v2(10))

