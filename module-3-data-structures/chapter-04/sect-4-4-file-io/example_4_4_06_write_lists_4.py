#Writing Lists 4
#Pprinting variables directly followed by a list.

myInt1 = 12
myInt2 = 23
myInt3 = 34
myList = ["David", "Lucy", "Vrushali", "Ping"
          "Natalie", "Dana", "Addison", "Jasmine"]

#Open OutputFile.txt in write mode
outputFile = open("OutputFile.txt", "w")

#Writes myInt1 to outputFile
outputFile.write(str(myInt1) + "\n")
#Writes myInt2 to outputFile
outputFile.write(str(myInt2) + "\n")
#Writes myInt3 to outputFile
outputFile.write(str(myInt3) + "\n")
#Joins myList using \n, then writes it to a file
outputFile.write("\n".join(myList))

outputFile.close()

#Output is 
# 12
# 23
# 34
# David
# Lucy
# Vrushali
# PingNatalie
# Dana
# Addison
# Jasmine