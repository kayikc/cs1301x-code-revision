# Save and Load function
# Principle:  

   # When we write code to save and load data, we usually follow a matching pattern:

   # If we save data FROM variable X TO a file
   # We later load that data FROM the file BACK TO variable X

# Saves inList to the file
def save(filename, inList):
   outputFile = open(filename, "w")
   # write the items in the input list to outputFile to save it.
   for item in inList:
      print(item, file= outputFile)
   
   outputFile.close()
   
#Loads from filename and returns a list of the contents
def load(filename):
   inputFile = open(filename, "r")
   inList =[] # see we're using the name 'inList' (the same name as that of save function)
   # but now this inList and that one of the save fucntion is not the same object though!
   
   for line in inputFile:
      inList.append(line.strip())
   inputFile.close()
   return inList

myList = ["David", "Lucy", "Vrushali", "Ping"
          "Natalie", "Dana", "Addison", "Jasmine"]

save("./output/OutputFile.txt", myList)
newList = load("./output/OutputFile.txt")

print(newList)
   
# #Output is
# ['David', 'Lucy', 'Vrushali', 'PingNatalie', 'Dana', 'Addison', 'Jasmine']
   
   