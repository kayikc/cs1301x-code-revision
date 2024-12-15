# Loading into List 2
# What happens if our file was a mixture of lists and variables?
myList =[]

inputFile = open("./output/OutputFile.txt", "r")

myInt1 = int(inputFile.readline()) #remember with int(), no need to use strip()
myInt2 = int(inputFile.readline())
myInt3 = int(inputFile.readline())
#For each line in the file
for line in inputFile:
   #Add the line to myList, stripping out whitespace
   myList.append(line.strip())

print(myInt1)
print(myInt2)
print(myInt3)
print(myList)

inputFile.close()

# Output is (OutputFile.txt has nothing to with that OutputFile.txt with the last question)
# 12
# 23
# 34
# ['David', 'Lucy', 'Vrushali', 'Ping', 'Natalie', 'Dana', 'Addison', 'Jasmine']

