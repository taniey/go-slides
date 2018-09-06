'''
    斐波那契数列即著名的兔子数列：1、1、2、3、5、8、13、21、34
'''

def fib_v1(max_value):
    a, b = 0, 1
    while b < max_value:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib_v2(max_value):
    arr = []
    for x in range(max_value):
        # 第1 2项都为1
        if x == 0 or x == 1:
            arr.append(1)
        else:
            arr.append(arr[-2] + arr[-1])
    print(arr)

def fib_yield(max_cnt):
    init_cnt, prev, curr = 0, 0, 1
    while init_cnt < max_cnt:
        yield curr
        prev, curr = curr, prev + curr
        init_cnt += 1


def main():

    # 方式1
    # fib_v1(100)

    # 方式2
    # fib_v2(10)

    # 方式3 yield
    # for x in fib_yield(10):
    #     print(x)
    print([ x for x in fib_yield(10)  ])








if __name__ == '__main__':
    main()