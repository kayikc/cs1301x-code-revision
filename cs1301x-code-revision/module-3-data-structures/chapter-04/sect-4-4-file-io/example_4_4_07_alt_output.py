#Another Way to Output
#A more intuitive way to outfiles using print() function

myList = ["David", "Lucy", "Vrushali", "Ping"
          "Natalie", "Dana", "Addison", "Jasmine"]

#Open OutputFile.txt in write mode
outputFile = open("OutputFile.txt", "w")

#For each name in myList
for name in myList:
   #You want to print each 'name', but print it to 'outputFile'
   #instead of the console.
   print(name, file = outputFile)

outputFile.close()

#Output is 
# David
# Lucy
# Vrushali
# PingNatalie
# Dana
# Addison
# Jasmine
