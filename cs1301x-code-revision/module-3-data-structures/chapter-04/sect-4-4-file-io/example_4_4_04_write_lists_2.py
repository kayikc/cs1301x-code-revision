# Writing Lists 2

myList = ["David", "Lucy", "Vrushali", "Ping"
          "Natalie", "Dana", "Addison", "Jasmine"]

#Open OutputFile.txt in write mode
outputFile = open("OutputFile.txt", "w")

#Writes every string in myList to a file
outputFile.writelines(myList)

outputFile.close()

#Output is DavidLucyVrushaliPingNatalieDanaAddisonJasmine
#Ops! No space between each item of the list.
#We can solve this by using .join
