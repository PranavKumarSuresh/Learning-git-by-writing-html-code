
from abc import ABCMeta,abstractmethod


class Shape(metaclass = ABCMeta):

	@abstractmethod
	def area(self):
		return 0

	

class Square(Shape):
	side = 4
	#def area(self):
		#print("area is:", self.side*4)


class Eqtriangle(Shape):
	side = 20
	def area(self):
		print("area is:", self.side*3)


eq = Eqtriangle()
sq = Square()

#sq.area()
eq.area()
