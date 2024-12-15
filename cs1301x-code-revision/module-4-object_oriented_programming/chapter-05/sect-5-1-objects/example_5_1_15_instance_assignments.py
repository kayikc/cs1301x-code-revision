# An instance of the Person class is mutable, so
# when we say myPerson2 = myPerson1, we’re really just telling them to look at
# the same data in memory. 

class Person:
  def __init__(self, name, eyecolor, age):
    self.name = name
    self.eyecolor = eyecolor
    self.age = age
    
class Name:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname
    
myPerson1 = Person(Name("David", "Joyner"), "brown", 30)
myPerson2 = myPerson1
myPerson2.eyecolor = "blue"
print("myPerson1's eyecolor: " + myPerson1.eyecolor)
print("myPerson2's eyecolor: " + myPerson2.eyecolor)

# Output:
# myPerson1's eyecolor: blue
# myPerson2's eyecolor: blue
