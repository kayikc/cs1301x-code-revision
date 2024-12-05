#Define the class Person:
class Person:
  #Crate a new instance of Person
  def __init__(self):
    #Person's default vales:
    self.firstname = "[no first name]"
    self.lastname = "[no last name]"
    self.eyecolor = "[no eye color]"
    self.age = -1
    
# Creae 2 new Persons and assign it to myPerson1 and myPerson2
myPerson1 = Person()
myPerson2 = Person()
myPerson1.firstname = "David"
myPerson2.firstname = "Vrushali"

print("myPerson1: " + myPerson1.firstname)
print("myPerson2: " + myPerson2.firstname)

# output is:
# myPerson1: David
# myPerson2: Vrushali