#Writing Lists 3

myList = ["David", "Lucy", "Vrushali", "Ping"
          "Natalie", "Dana", "Addison", "Jasmine"]

#Open OutputFile.txt in write mode
outputFile = open("OutputFile.txt", "w")

#Writes every string in myList to a file
outputFile.write("\n".join(myList))

outputFile.close()

#Output is 
# David
# Lucy
# Vrushali
# PingNatalie
# Dana
# Addison
# Jasmine
