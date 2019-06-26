a = 1
b = 1
a == b # True
a is b # True

a = 888
b = 888
a == b # True
a is b # False

a = 'hello'
b = 'hello'
a is b # True
a == b # True

a = 'hello world'
b = 'hello world'
a == b # True
a is b # False