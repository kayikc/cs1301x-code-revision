# When a new Person is created, Python uses the __init__ method to initialise
# instance variables like firstname and lastname with the provided values.
# IMPORTANT: Variables prefixed with `self` are instance-specific and persist for the object,
# while parameters like `firstname` are temporary and only exist during method execution.

class Person: 
    # Initialises a new Person object with given attributes.
    def __init__(self, firstname, lastname):
        self.firstname = firstname  # Instance variable for first name
        self.lastname = lastname    # Instance variable for last name
        self.eyecolor = "[no eye color]"  # Default eye color
        self.age = -1  # Default age

# Creates a Person instance with firstname="David" and lastname="Joyner"
myPerson = Person("David", "Joyner")
print(myPerson.firstname) 
print(myPerson.lastname)

# Output is:
# David
# Joyner
