list = [1, 3, 3, 3, 3]
print("Before list {}".format(list))

c = 0
for i in list:
    if i == 3:
        list.remove(i)
        c += 1

print('After list {}'.format(list))
print('delete count of 3: {}'.format(c))
