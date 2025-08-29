class Father:
	def skills(self):
		print("Gardening, Fishing")

class Mother:
	def skills(self):
		print("Cooking, Painting")

class Child(Father, Mother):
	def skills(self):
		print("Child's combined skills:")
		Father.skills(self)
		Mother.skills(self)

c= Child()
c.skills()

