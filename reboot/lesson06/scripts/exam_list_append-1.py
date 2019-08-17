arr1 = ['www', '51reboot', 'com']
arr2 = arr1
print(arr1 is arr2) # 比较对象地址是否相同

arr1.append('cn')
print(arr1)
print(arr2)