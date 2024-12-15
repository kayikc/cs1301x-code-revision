# Simple File Reading 3
# 1. readline() reads exactly what's in the file including its newline character (\n)
#    e.g., if line in file is "12\n", readline() gives us "12\n"
# 2. print() automatically adds its own \n after printing
# 3. Without strip(), we get double spacing because we have:
#    - One \n from the file (through readline)
#    - One \n from print()
# 4. strip() removes the file's \n, so we only get print()'s \n

inputFile = open("./output/OutputFile.txt", "r")

#Print the next line of inputFile, strip() removes file's \n, print() adds one \n
print(inputFile.readline().strip())
#Print the next line of inputFile, strip() removes file's \n, print() adds one \n
print(inputFile.readline().strip())
#Print the next line of inputFile, strip() removes file's \n, print() adds one \n
print(inputFile.readline().strip())

# Output is now single-spaced (only print's \n):
# 12
# 23
# 34
# instead of double-spaced (file's \n + print's \n):
# 12

# 23

# 34
