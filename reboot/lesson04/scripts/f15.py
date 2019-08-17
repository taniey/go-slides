def f(x, *args, **kwargs):
	print(x, args, kwargs)

f(1, 2, 3, x=4, y=5)


