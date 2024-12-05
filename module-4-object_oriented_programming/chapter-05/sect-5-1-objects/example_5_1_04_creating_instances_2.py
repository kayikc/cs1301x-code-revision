#Define the class Person:
class Person:
  def __init__(self):
    self.firstname = "[no first name]"
    self.lastname = "[no last name]"
    self.eyecolor = "[no eye color]"
    self.age = -1
    
# Creae a new Person and assign it to myPerson
myPerson = Person()

print(myPerson.firstname)

# Change myPerson's firstname to David
myPerson.firstname = "David"

print(myPerson.firstname)

#output is:
# [no first name]
# David
