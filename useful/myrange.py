# def myrange(start,stop=None,step=1):
# 	if stop==None:
# 		stop=start
# 		start=0
# 	i=start	
# 	while i<stop:
# 		yield i
# 		i+=step
# print(list(myrange(5,9)))

class Tree:
	def __init__(self, val=None, depth=0):
		self.val = val
		self.d = depth

	def __repr__(self):
		return str(self.val)

	def l(self, val):
		self.l = Tree(val, self.d+1)
	def r(self, val):
		self.r = Tree(val, self.d+1)
