# Creates myDictionary with key-values below
myDictionary = {
   "sprockets" : 5,
   "widgets": 11,
   "cogs" : 3,
   "gizmos": 15,
   "gadgets": 1
}
# Iterate over the keys() and values() simultaneously
# items()
for (key, value) in myDictionary.items():
   if value < 5:
      print(key, "is less than 5:", value)

# #Output is
# cogs is less than 5: 3
# gadgets is less than 5: 1