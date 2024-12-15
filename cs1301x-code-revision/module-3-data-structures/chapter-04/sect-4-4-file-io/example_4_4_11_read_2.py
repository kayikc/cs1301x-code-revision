# Simple File Reading 2
# To print the contents, we have to actually read the file
# readline() reads, and to the next line break (so it includes \n)
inputFile = open("./output/OutputFile.txt", "r")

#Print the next line of inputFile
print(inputFile.readline())
#Print the next line of inputFile
print(inputFile.readline())
#Print the next line of inputFile
print(inputFile.readline())

inputFile.close()

#Output is (I made a new OutputFile.txt and put 3 integers in it)

# 12

# 23

# 34