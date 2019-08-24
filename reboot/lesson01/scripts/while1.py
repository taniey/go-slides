total = 0
num = 1
while num <= 10:
    num = num + 1
    total = total + num

print(total)

# have else case
total = 0
num = 1
while num <= 10:
    num = num + 1
    total = total + num

    if (total > 50):
        print("total: bigger then 50 , current total: ", total)
        break

else:
    print(total)
