# Creates myDictionary with key-values below
myDictionary = {
   "sprockets" : 5,
   "widgets": 11,
   "cogs" : 3,
   "gizmos": 15,
   "gadgets": 1
}
# Iteration through keys is more commonly used than just values
# Iterate over the keys() directly
for key in myDictionary.keys():
   value = myDictionary[key]
   if value < 5:
      print("A value less than 5 was found:", value)

# #Output is
# A value less than 5 was found: 3
# A value less than 5 was found: 1