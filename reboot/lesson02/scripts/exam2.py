'''
让用户从控制台输入format: name, age, tel
ID => 现有用户的最大ID + 1
'''

db = ('monkey', '51reboot')

userinfo = [
    (1, 'monkey', 25, '132xxxx', 'beijing'),
]

while True:
    username = input("please input your username: ")
    password = input("please input your password: ")
    if username == db[0] and password == db[1]:

        while True:
            txt = input("please input user info(name age tel address):")
            nodes = txt.split()
            if len(nodes) != 4:
                errmsg = "input msg error."
                print(errmsg)
                continue
            else:
                if len(userinfo) == 0:
                    userinfo.append((1, nodes[0], nodes[1], nodes[2], nodes[3]))
                else:
                    max_uid = 0
                    for obj in userinfo:
                        if obj[0] > max_uid:
                            max_uid = obj[0]
                    userinfo.append((max_uid+1, nodes[0], nodes[1], nodes[2], nodes[3]))
            print(userinfo)
    else:
        errmsg = "username or password invalid."
        print(errmsg)
        continue
