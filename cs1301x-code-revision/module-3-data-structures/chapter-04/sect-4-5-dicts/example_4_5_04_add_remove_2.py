# Creates myDitionary with David=4045551234, Lucy=4045555678
# Vrushali=4045559101
myDicionary ={
   "David": 4045551234,
   "Lucy": 4045555678,
   "Vrushali": 4045559101
}
print(myDicionary)

# Checks if "David" is a key in the dicionary
# The "in" operator operates on the keys of the dictionary
if "David" in myDicionary:
   print("David is already in myDictionary!")
   myDicionary["David2"] = "4045551121"
else:
   myDicionary["David"] = "4045551121"
print(myDicionary)

#Output is 
# {'David': 4045551234, 'Lucy': 4045555678, 'Vrushali': 4045559101}
# David is already in myDictionary!
# {'David': 4045551234, 'Lucy': 4045555678, 'Vrushali': 4045559101, 'David2': '4045551121'}