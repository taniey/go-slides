

'''
1 * 1 = 1
1 * 2 = 2 2 * 2 = 4
1 * 3 = 3 2 * 3 = 6 3 * 3 = 9
1 * 4 = 4 2 * 4 = 8 3 * 4 = 12 4 * 4 = 16


n * m = (n * m)

m 代表行
1 * m = m ....... m * m = m^

1 * 9 = 9 ....... 9 * 9 = 81
'''

'''
for m in range(1, 10):
    i = 1
    while i <= m:
        print("{} * {:2} = {:2}".format(i, m, i * m), end=' ')
        i += 1
    print()
'''




m = 1

while m <= 9:
    i = 1
    while i <= m:
        print("{} * {} = {}".format(i, m, i * m), end=' ')
        i += 1
    print()
    m += 1
