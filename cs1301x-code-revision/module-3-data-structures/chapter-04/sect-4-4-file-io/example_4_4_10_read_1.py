# Simple File Reading 1
# ? Python prints a reference to what type of file is and what mode it’s
# in, not the contents. 

#Please change to the path where you save the OutputFile.txt
#Also pay attention to where you're at now.
inputFile = open("./output/OutputFile.txt", "r")
print(inputFile)
inputFile.close()

# #Output is
# <_io.TextIOWrapper name='.\\OutputFile.txt' mode='r' encoding='cp1252'>