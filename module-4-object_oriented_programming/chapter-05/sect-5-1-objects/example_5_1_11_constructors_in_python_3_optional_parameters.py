# we’ve defined the parameters as optional by giving them
# default values in the parameter list. If a given argument isn’t supplied, the code
# assumes it should use the value from the parameter list (such as “[no first name]”
# for firstname on line 4)

class Person: 
    def __init__(self, firstname = "[no first name]"
                     , lastname = "[no last name]"):
        self.firstname = firstname 
        self.lastname = lastname           
        self.eyecolor = "[no eye color]" 
        self.age = -1  

myPerson1 = Person() # <- no positional arguments provided
print(myPerson1.firstname) 

myPerson2 = Person(firstname = "David") 
print(myPerson2.firstname) 

myPerson3 = Person("Vrushali") # <- assumes first positional argument 'firstname'
print(myPerson3.firstname)

# Output is:
# [no first name]
# David
# Vrushali

