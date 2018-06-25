class Apple:
	def __init__(self):
		self.manufacturer =  "Apple inc"
		self.site = "www.apple.com/comtac"

	

	def cont(self,site):
		print("to contact:",self.manufacturer,self.site)

class Macbook(Apple):
	

	def mfgDetails(self,yom):
		self.yom = yom
		print("details",self.yom,self.manufacturer,self.site)


macbook = Macbook()
macbook.mfgDetails(2017)
macbook.cont(site = 10)