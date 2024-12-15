# Simple File Reading 4
# Further demonstrate readline() and the need to strip the \n off that comes with it
# input() not only cast string to integer, it also ignores whitespace

inputFile = open("./output/OutputFile.txt", "r")

#Pay attention to the int casting method, it automatically ignore the whitespace in the strings
#that means we don't need the .strip() method anymore if we ue int()
#Read the next line of inputFile, cast it to int, and assign it to myInt1
myInt1 = int(inputFile.readline()) # int() instead of .strip()
#Read the next line of inputFile, cast it to int, and assign it to myInt2
myInt2 = int(inputFile.readline())
#Read the next line of inputFile, cast it to int, and assign it to myInt3
myInt3 = int(inputFile.readline())

print("myInt1:", myInt1)
print("myInt2:", myInt2)
print("myInt2:", myInt3)

inputFile.close()

#You see how myInt1: 12 and then starts a newline? Same for myInt2 and myIn3. 
# It's because of the \n from readline()
# Output is
# myInt1: 12
# myInt2: 23
# myInt2: 34