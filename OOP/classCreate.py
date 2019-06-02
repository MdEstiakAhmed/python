class Car:
	name = ""		# name is a class attribute. this can access by Car.name
	color = ""

	def __init__(self, engine, petrol):		# this is constructor
		self.engine = engine		# engine is a instance attribute. this can access only by object. not by Class name.
		self.petrol = petrol

	def startcar(self):
		print("start car")

	def details(self):
		print("car name: ", self.name)
		print("car color: ", self.color)
		print("car model: ",self.model)
		print("car engine: ", self.engine)
		print("car petrol: ", self.petrol)


c1 = Car("100CC", "50L")		# object
c2 = Car("150CC", "75L")		# object

c1.model = 2017		# can be also declare variable with object
c2.model = 2015

c1.name = "alion"		# variable declare
c2.name = "corolla"

c1.color = "white"
c2.color = "black"

c1.details()
c1.startcar()

print()

c2.details()
c2.startcar()
