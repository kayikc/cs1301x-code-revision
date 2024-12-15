myString = """
   This is the string whose words we would like to count. \
This string contains some repeated words, as well as some unique words. It contains \
punctuation, and it contains words that are capitalised in different ways. If the \
method we write runs correctly, it will count 4 instances of the word 'it'. 3 instances \
of the word 'this', and 3 instances of the 'count'. 
"""

myString = myString.replace(".","") # Remove periods
myString = myString.replace(",","") # Remove commas
myString = myString.replace("'","") # Remove apostrophes
myString = myString.lower() # Male all lower case
mySplitString = myString.split() # Split by spaces

wordDiciontary = {} #Create empty dicitonary
for word in mySplitString:
   if word in wordDiciontary:
      wordDiciontary[word] += 1
   else:
      wordDiciontary[word] = 1
      
print(wordDiciontary) 

#Output is 
# {'this': 3, 'is': 1, 'the': 5, 'string': 2, 'whose': 1, 'words': 4, 
# 'we': 2, 'would': 1, 'like': 1, 'to': 1, 'count': 3, 'contains': 3, 
# 'some': 2, 'repeated': 1, 'as': 2, 'well': 1, 'unique': 1, 'it': 4,
# 'punctuation': 1, 'and': 2, 'that': 1, 'are': 1, 'capitalised': 1, 
# 'in': 1, 'different': 1, 'ways': 1, 'if': 1, 'method': 1, 'write': 1, 
# 'runs': 1, 'correctly': 1, 'will': 1, '4': 1, 'instances': 3, 'of': 3, 
# 'word': 2, '3': 2}      
