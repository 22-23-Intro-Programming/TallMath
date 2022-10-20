
class MyAnimal:
	def __init__(self, name, specie, height, SP):         #the initial property of all objects in this class
		self.name = name
		self.specie = specie
		self.height = height
		self.SP = SP
	def UseSuperPower(self):
		print(self.name + " had used " + self.SP)

def main():
    Pierka = MyAnimal("{Pierka}", "Dinosaur", 10.2, "SuperStriking")
    print("Hey, you want to see my super cute animal?")
    print("It's a " + Pierka.specie + ".")
    print("Now he's going to show off something.")
    Pierka.UseSuperPower()
if __name__ == "__main__":
	main()
