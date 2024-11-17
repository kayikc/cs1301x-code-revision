# Using named keys in dictionaries (like "phone", "address") instead of numeric indices 
# makes code more maintainable than remembering position numbers for each value. 
# This approach mimics basic object-oriented design, 
# where data is organised with meaningful labels rather than sequential positions.

ANSWER_KEY = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "A"}

students = {}
students["David"] = {"1": "A", "2": "B", "3": "A", "4": "B", "5": "C"}
students["Terra"] = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "A"}
students["Lugos"] = {"1": "A", "2": "C", "3": "C", "4": "D", "5": "A"}

for (student, answers) in students.items():
   grade = 0
   for (question, answer) in answers.items():
      if answer == ANSWER_KEY[question]: # "question" is the key
         grade += 1
         
   students[student]["grade"] = grade

for (student, answers) in students.items():
   print(student, ": ", answers["grade"], sep = "", end ="; ")

# Output
# # David: 2: Terra: 5: Lugos: 4: 

# Side note:
# While modern Python (3.7+) preserves dictionary insertion order,
# it's good practice to write code that doesn't depend on dictionary order
