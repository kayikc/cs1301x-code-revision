# Name instances are mutable - when we pass myPerson1.name to construct myPerson2,
# both objects point to the same Name instance in memory. Changes to one affect both
# since they share the same underlying mutable object.
class Person:
   def __init__(self, name, eyecolor, age):
       self.name = name
       self.eyecolor = eyecolor
       self.age = age

class Name:
   def __init__(self, firstname, lastname):
       self.firstname = firstname
       self.lastname = lastname

# Create person1 and person2 that share the same Name instance
myPerson1 = Person(Name("David", "Joyner"), "brown", 30)
myPerson2 = Person(myPerson1.name, myPerson1.eyecolor, myPerson1.age)

# Changing eyecolor only affects myPerson2
myPerson2.eyecolor = "blue"
print(myPerson1.eyecolor)  # brown - unchanged
print(myPerson2.eyecolor)  # blue - changed

# Changing firstname in person1 affects person2 since they share the same Name object
myPerson1.name.firstname = "Vrushali"
print(myPerson1.name.firstname)  # Vrushali
print(myPerson2.name.firstname)  # Also Vrushali - same object reference