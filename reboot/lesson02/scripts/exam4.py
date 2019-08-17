

import random


guess = random.randint(1, 100)

count = 0


while count < 7:
    num = int(input('please input a number: '))
    if num == guess:
        print("你太聪明了")
    elif num > guess:
        print("你猜大了")
    else:
        print("你猜小了")
    count += 1
