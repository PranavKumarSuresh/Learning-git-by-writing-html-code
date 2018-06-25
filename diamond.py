class A:
	def meth(self):
		print("from A")

class B(A):
	def meth(self):
		print("from B")
	pass


class C(A):
	def meth(self):
		print("from C")

class D(B,C):
	pass



d = D()
d.meth()
