# The __init__ method takes two mandatory positional arguments: firstname and lastname.
# These must be provided when creating a Person object.

class Person: 
    def __init__(self, firstname, lastname):
        self.firstname = firstname  # Instance variable for first name
        self.lastname = lastname    # Instance variable for last name
        self.eyecolor = "[no eye color]"  # Default eye color
        self.age = -1  # Default age

# LOOK HERE: # This will cause an error because firstname and lastname are required.
myPerson = Person() # <- missing positional arguments firstname and lastname
print(myPerson.firstname) 
print(myPerson.lastname)

# Output is:
# TypeError: Person.__init__() missing 2 required positional arguments: 'firstname' and 'lastname'

# Next, we will see how to make the parameters optional
