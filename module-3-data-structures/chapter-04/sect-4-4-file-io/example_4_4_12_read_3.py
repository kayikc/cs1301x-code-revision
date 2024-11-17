# Simple File Reading 3
# readline() moves the reader forward to the start of the next line, 
# so when we call readline(), the next line is passed permanently;
# IMPORTANT:  if we want to store or print the lines without the line breaks
# we need to strip the whitespace off of them

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