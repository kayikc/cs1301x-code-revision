#Appending to Files 2
#If we run the previous code (4_4_8) twice, then each of the three lines is printed twice. 
#If we run it three more times, then each of the three lines will be printed three more

myList = ["David", "Lucy", "Vrushali", "Ping"
          "Natalie", "Dana", "Addison", "Jasmine"]

#Open OutputFile.txt in append mode
outputFile = open("OutputFile.txt", "a")

#For each name in myList
for name in myList:
   # Write the name the file on its own line
   print(name, file = outputFile)

outputFile.close()

#Output is (beware that it's the result of this script to the OutputFile.txt from 4_4_8_AppendingtoFiles.py)
#and the output from
# David
# Lucy
# Vrushali
# PingNatalie
# Dana
# Addison
# Jasmine
# 12
# 23              
# 34
# David             <-- newly appended
# Lucy              <-- newly appended
# Vrushali          <-- newly appended  
# PingNatalie       <-- newly appended 
# Dana              <-- newly appended  
# Addison           <-- newly appended 
# Jasmine           <-- newly appended
