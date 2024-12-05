# from Joyner Introduction to Computing 1st Edition
# On line 4, __init__ is Python’s convention for identifying constructors.
# Whenever a new instance of a class is created, Python goes and searches for the
# class’s __init__ method and runs it if it exists. If it doesn’t exist, that’s alright;
# Python just creates the instance without running any initial code. Here, running this
# constructor creates the variables firstname, lastname, eyecolor, and age to be
# seen later    

class Person: 
  #Create a new instance of Person
  def __init__(self):
    self.firstname = "[no first name]"
    self.lastname = "[no last name]"
    self.eyecolor = "[no eye color]"
    self.age = -1
    