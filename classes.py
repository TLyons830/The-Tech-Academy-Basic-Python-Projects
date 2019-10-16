

# parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg

# child class instance
class Human(Organism):
    name = 'MacGuyver'
    species = 'Homosapien'
    legs = 2
    arms = 2
    origin = "Earth"

    def ingenuity(self):
        msg = "\n{} Creates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!".format(self.name)
        return msg

# another child class instance
class Dog(Organism):
    name = 'Spot'
    species = 'Canine'
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"

    def bite(self):
        msg = "\nEmits a loud growl and bites on it's target!"
        return msg

# another child class instance

class Bacterium(Organism):
    name = 'X'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = "Mars"

    def replication(self):
        msg = "\nCells divide and multiply!"
        return msg





if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())
