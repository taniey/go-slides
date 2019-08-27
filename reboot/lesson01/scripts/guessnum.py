# -*- coding: utf-8 -*-
'''guess the num'''

# from random import randint
import random


def main():
    '''the guess function'''
    can_retry_count = 6
    thenum = random.randint(0, 100)
    # thenum = random.randrange(0, 101)
    # print(type(thenum))

    while can_retry_count > 0:
        print("you have", can_retry_count, "chance!")
        guess_str = input("please input a num [0, 100]: ")
        try:
            guess = int(guess_str)
            if guess > thenum:
                print("( big )")
            elif guess < thenum:
                print("( small )")
            else:
                print("that's right! will exit. ")
                break
        except ValueError:
            print("input error!!!!!!")

        # set
        can_retry_count = can_retry_count - 1

    else:
        print("you losed.")


if __name__ == '__main__':
    main()
