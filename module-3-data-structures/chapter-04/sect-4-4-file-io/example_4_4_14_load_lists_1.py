# Loading into List 1
# The challenge for reading is that we don't know in advance how many lines there are to read.

myList =[]

inputFile = open("./output/OutputFile.txt", "r")

#For each line in the file
for line in inputFile:
   #Add the line to myList, stripping out whitespace
   myList.append(line.strip())

print(myList)

inputFile.close()

# Output is
# ['12', '23', '34']
