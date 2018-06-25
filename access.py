class Car:
	wheels = 4
	_color = "black"
	__yom = 2017

	
	print (__yom)

class Bmw(Car):
	def __init__(self):
		print("protexted attrobite: ", self._color)


car = Car()
print("public attribute: ",car.wheels)

bmw = Bmw()
print("protexted attrobite: ", bmw._color)


