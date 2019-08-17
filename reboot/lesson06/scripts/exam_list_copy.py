arr = ['www', '51reboot', 'com', ['www', 'baidu']]
print(id(arr))
print([id(i) for i in arr])

arr2 = arr.copy()
print(id(arr2))
print([id(i) for i in arr2])