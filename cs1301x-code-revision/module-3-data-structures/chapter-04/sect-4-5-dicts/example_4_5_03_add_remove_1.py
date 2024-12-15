# Creates myDictionary with key-value below

myDictionary = {
   "sprockets" : 5,
   "widgets": 11,
   "cogs" : 3,
   "gizmos": 15
}

print(myDictionary)
# {'sprockets': 5, 'widgets': 11, 'cogs': 3, 'gizmos': 15}

#Creates the newkey "gadgets" with value 1
myDictionary["gadgets"] = 1
print(myDictionary)
# {'sprockets': 5, 'widgets': 11, 'cogs': 3, 'gizmos': 15, 'gadgets': 1}

del myDictionary["gadgets"]
print(myDictionary)
# {'sprockets': 5, 'widgets': 11, 'cogs': 3, 'gizmos': 15}