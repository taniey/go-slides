s = '1234567890-'

for x in s:
    print(x)
else:
    print("finished")

print("==============")

# not exec else
for x in s:
    print(x)
    if x == '0':
        print('in if x== 0 will not execute else case')
        break
else:
    print("else case executed , finished")
