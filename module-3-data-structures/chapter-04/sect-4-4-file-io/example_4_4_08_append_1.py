#Appending to Files
#Computer opens the file in "a" mode and start from sratch

myInt1 = 12
myInt2 = 23
myInt3 = 34

#Open OutputFile.txt in append mode
outputFile = open("OutputFile.txt", "a")

#Write myInt1 to outputFule
outputFile.write(str(myInt1) + "\n")
#Write myInt2 to outputFule
outputFile.write(str(myInt2) + "\n")
#Write myInt3 to outputFule
outputFile.write(str(myInt3) + "\n")
#Close outputFile
outputFile.close()

#Output is (beware that it's the result of this script to the OutputFile.txt from 4_4_7_AnotherWaytoOutput.py)
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

# 12             <-- newly appended
# 23             <-- newly appended
# 34             <-- newly appended  
