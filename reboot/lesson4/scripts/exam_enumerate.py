nameList = ["xiaoming", "xiaohong", "xiaoli", "xiaowang"]

idx = 1
for name in nameList:
    print(idx, name)
    idx += 1

print("------------v1-------------")

for i in range(0, len(nameList)):
    print(i, nameList[i])

print("------------v2-------------")

for i, info in enumerate(nameList):
    print(i, info)

print("------------v3-------------")