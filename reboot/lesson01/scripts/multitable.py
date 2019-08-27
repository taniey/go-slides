# -*- coding: utf-8 -*-
'''the first multiplication table'''


def main():
    '''print multiplication table'''
    for i in range(1, 9 + 1):
        for j in range(1, i + 1):
            result = i * j
            print(i, end=' ')
            print("*", end=' ')
            print(j, end=' ')
            print("=", end=' ')
            print(result, end=' ')
            print("\t", end=' ')
            # print(i, "*", j, "=", result, "\t", end=" ")

        print("")


if __name__ == '__main__':
    main()
