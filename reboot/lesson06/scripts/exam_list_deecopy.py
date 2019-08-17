import copy

arr = ['www', '51reboot', 'com', ['www', 'baidu']]
print(id(arr))
print([id(i) for i in arr])

arr2 = copy.deepcopy(arr)
print(id(arr2))
print([id(i) for i in arr2])