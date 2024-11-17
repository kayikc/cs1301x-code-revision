# Use Lists with Dictionary
classes = {
   "Math" : ["David", "Lucy","Dana"],
   "Physics" : ["Addison", "Vrushali", "Bilbo"],
   "Chemistry" : ["Sara", "Lugos", "Mireia", "Perle"],
   "Computing" : ["Partha", "Venijamin", "Terra", "Sofia"],
   "History" : ["Tryphon", "Gevorg", "Raza", "Rein"],
}

print("Students in Computing:", classes["Computing"])
#Add Francies to History
classes["History"].append("Francies")
print("Students in History:", classes["History"])

# #Output is
# Students in Computing: ['Partha', 'Venijamin', 'Terra', 'Sofia']
# Students in History: ['Tryphon', 'Gevorg', 'Raza', 'Rein', 'Francies']