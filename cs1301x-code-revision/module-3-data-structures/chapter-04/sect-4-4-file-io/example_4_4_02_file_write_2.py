# Simple File Writing 2
myInt1 = 12
myInt2 = 23
myInt3 = 34

#Open OutputFile.txt in writing mode
#We give it a name "OutputFile.txt"
outputFile = open("OutputFile.txt","w")

#Write myInt1 to outputFile
outputFile.write(str(myInt1) + "\n")
#Write myInt2 to outputFile
outputFile.write(str(myInt2) + "\n")
#Write myInt3 to outputFile
outputFile.write(str(myInt3) + "\n")
#Close outputFile
#Close the file to prevent others from not being able to open it
outputFile.close()

#Output is an OutputFile.txt in which the content is 
# 12
# 23
# 34
#Due to writing mode, the previous OutputFile.txt is overwritten by this OutputFile.txt.