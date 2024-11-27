# Simple File Reading 3
# readline() reads and returns an entire line, including the newline character (\n) at the end
# Each subsequent readline() moves the file pointer to the start of the next line
# To avoid double spacing when printing, we use strip() to remove the \n that comes from the file
# (print() will still add its own newline automatically)

inputFile = open("./output/OutputFile.txt", "r")

# Print first line without the file's \n character
print(inputFile.readline().strip())
# Print second line without the file's \n character
print(inputFile.readline().strip())
# Print third line without the file's \n character
print(inputFile.readline().strip())

# Output is now
# 12
# 23
# 34
# instead of
# 12

# 23

# 34
# like in 4_4_11
inputFile = open("./output/OutputFile.txt", "r")

#Print the next line of inputFile
print(inputFile.readline().strip())
#Print the next line of inputFile
print(inputFile.readline().strip())
#Print the next line of inputFile
print(inputFile.readline().strip())

# Output is now
# 12
# 23
# 34
# instead of
# 12

# 23

# 34
# like in 4_4_11