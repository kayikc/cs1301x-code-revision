# Simple File Writing 1
myInt1 = 12
myInt2 = 23
myInt3 = 34

#Open OutputFile.txt in writing mode
#We give it a name "OutputFile.txt"
outputFile = open("OutputFile.txt","w")

#Write myInt1 to outputFile
outputFile.write(str(myInt1))
#Write myInt2 to outputFile
outputFile.write(str(myInt2))
#Write myInt3 to outputFile
outputFile.write(str(myInt3))
#Close outputFile
#Close the file to prevent others from not being able to open it
outputFile.close()

#Output is an OutputFile.txt in which the content is 122334