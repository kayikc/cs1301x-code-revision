# Writing Lists 1
myList = ["David", "Lucy", "Vrushali", "Ping"
          "Natalie", "Dana", "Addison", "Jasmine"]

#Open OutputFile.txt in write mode
outputFile = open("OutputFile.txt", "w")

#For each name in myList
for name in myList:
   #Write the name to the file on its own line
   #With a line break one each one! (writeline would be easier though!)
   outputFile.write(name + "\n")
   
outputFile.close()

#Next up, we'll see how writeline does the same thing but easier.