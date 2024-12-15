# Unlike previous example, we create a new Name instance for myPerson2 by passing 
# the immutable string values (firstname, lastname) rather than the mutable Name object.
# This means changes to myPerson2's name won't affect myPerson1's name.
class Person:
   def __init__(self, name, eyecolor, age):
       self.name = name
       self.eyecolor = eyecolor
       self.age = age

class Name:
   def __init__(self, firstname, lastname):
       self.firstname = firstname
       self.lastname = lastname

# Create person1 with its own Name instance
myPerson1 = Person(Name("David", "Joyner"), "brown", 30)

# Create person2 with a NEW Name instance using person1's string values
myPerson2 = Person(Name(myPerson1.name.firstname, myPerson1.name.lastname),
                 myPerson1.eyecolor, myPerson1.age)

myPerson2.eyecolor = "blue"
print(myPerson1.eyecolor)    # brown - unchanged
print(myPerson2.eyecolor)    # blue - changed

# Changing person2's name doesn't affect person1 since they have separate Name objects
myPerson2.name.firstname = "Vrushali"
print(myPerson1.name.firstname)  # David - unchanged 
print(myPerson2.name.firstname)  # Vrushali - only person2 changed