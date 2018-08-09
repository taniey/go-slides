

retdata = []
actions = ['list', 'add', 'update', 'delete', 'find', 'exit']


while True:
    action = input("\nPlease input your action({}): ".format(actions))
    if action not in actions:
        print("invalid action, only support {}".format(actions))
        continue

    if action == 'list':
        '''
            list
        '''

    elif action == 'add':
        '''
            add zhengyscn 28 132xxxxxx
        '''

    elif action == 'update':
        '''
            update zhengyscn 26 131xx
        '''

    elif action == 'delete':
        '''
            delete zhengyscn
        '''

    elif action == 'find':
        '''
            find zhengyscn
        '''

    elif action == 'exit':
        print("Welcome back next time.")
        break