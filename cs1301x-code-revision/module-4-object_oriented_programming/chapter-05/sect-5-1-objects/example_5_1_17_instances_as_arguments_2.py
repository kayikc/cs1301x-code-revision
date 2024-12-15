# This code demonstrates how strings are immutable (unchangeable) in Python 
# and how this affects function behavior

class Person:
    def __init__(self, name, eyecolor, age):
        # Creates a person with a Name object, eye color, and age
        self.name = name
        self.eyecolor = eyecolor
        self.age = age

class Name:
    def __init__(self, firstname, lastname):
        # Stores a person's first and last name as strings
        self.firstname = firstname
        self.lastname = lastname

def capitalizeString(instring):
    # This function tries to convert a string to uppercase
    # BUT: Since strings are immutable, this only changes the local copy
    # and doesn't affect the original string
    instring = instring.upper()

# Create a person named "David Joyner" with brown eyes, age 30
myPerson = Person(Name("David", "Joyner"), "brown", 30)

# These calls don't change the original strings because strings are immutable
capitalizeString(myPerson.name.firstname)  # Tries to capitalize "David"
capitalizeString(myPerson.name.lastname)   # Tries to capitalize "Joyner"

# The original strings remain unchanged
print(myPerson.name.firstname)  # Prints: David
print(myPerson.name.lastname)   # Prints: Joyner

# When working with immutable types like strings,
# functions can't modify the original value. To change strings,
# you need to reassign the result back to the original variable.