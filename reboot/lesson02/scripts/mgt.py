'''
id  name age tel address
'''
'''
userinfo = [
    [1, 'monkey2', 20, '132xxx', 'beijing'],
    [2, 'monkey1', 20, '132xxx', 'beijing'],
    [3, 'monkey4', 20, '132xxx', 'shanghai'],
    [4, 'monkey7', 20, '132xxx', 'beijing'],
]
'''
userinfo = []
logininfo = ('admin', '51reboot')
count = 3

'''
break
'''

while True:
    print(userinfo)
    username = input("input login username: ")
    password = input("input login password: ")
    if username == logininfo[0] and password == logininfo[1]:
        op = input("input op: ")
        if op == 'add':
            '''
            body = ‘monkey3 22 132xxx shanghai’
            body.split(' ') 
            ['monkey2', '20', '132xxx', 'beijing']
            '''
            body = input("input user info: ")
            user_list = body.split(' ')  # str -> list
            if len(userinfo) == 0:
                user_list.insert(0, 1)
                userinfo.append(user_list)
            else:
                uids = [x[0] for x in userinfo]
                new_id = max(uids) + 1
                user_list.insert(0, new_id)
                userinfo.append(user_list)

        elif op == 'delete':
            '''
                delete 4
            '''
            uid = input("input uid: ")
            for x in userinfo:
                if x[0] == int(uid):
                    userinfo.remove(x)
        elif op == 'update':
            '''
            
            '''
        elif op == 'list':
            pass
        elif op == 'find':
            '''
            find 1
            find monkey2
            '''
        elif op == 'exit':
            print("-------退出信息-----------")
            break
        else:
            print("invalid op.")
    else:
        print("login failed.")
