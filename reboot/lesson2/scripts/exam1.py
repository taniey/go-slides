userlist = [
    (1, 'monkey1', 28, '132xxxx', 'beijing'),
    (2, 'monkey2', 23, '135xxxx', 'shanghai'),
    (3, 'monkey3', 21, '139xxxx', 'zhengzhou'),
]

'''

|   id  |   name    |   age |   tel |   address |
-------------------------------------

'''


'''
^   居中
<   左对齐
>   右对齐
'''

template = "|{0:^3}|{1:<10}|{2:^5}|{3:<15}|{4:<12}|"
splitline = '-'*51

print(template.format('id', 'name', 'age', 'tel', 'address'))
print(splitline)

for obj in userlist:
    print(template.format(obj[0], obj[1], obj[2], obj[3], obj[4]))

print(splitline)