class Animal:
	def breathe(self):
		print("Dog can breathe")
class Mammal(Animal):
	def walk(self):
		print("Dog can walk")
class Dog(Mammal):
	def bark(self):
		print("Dog can bark")

dog = Dog()

print("Dog Characteristics:")
dog.breathe() # Inherited from Animal
dog.walk() # Inherited from Mammal
dog.bark() # Defined in Dog

