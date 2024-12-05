#Define the class Name:
class Name:
  def __init__(self):
    self.firstname = "[no first name]"
    self.lastname = "[no last name]"

#Define the class Person:
class Person:
  def __init__(self):
    self.name = Name()
    self.eyecolor = "[no eye color]"
    self.age = -1
    
# Creae a new Person and assign it to myPerson
myPerson = Person()

print(myPerson.name.firstname) # .name from Person, .firstname from Name() inside Person

# Change myPerson's firstname to David
myPerson.name.firstname = "David"

print(myPerson.name.firstname)

#output is:
# [no first name]
# David
