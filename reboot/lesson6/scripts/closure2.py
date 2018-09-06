def println(msg):
	'''外层包围函数'''
	def printer():
		'''嵌套函数'''
		print(msg)
	printer()

println("51reboot")