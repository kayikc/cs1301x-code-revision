# Use Tuples with Dictionary
addressBook = {
   "David" : ("555 Home St", "4045551234", "david@david.com"),
   "Lucy" : ("555 Home St", "404555678", "lucy@lucy.com"),
   "Dana" : ("123 There Rd", "4045559101", "dana@dana.com"),
}
# Pay attention to Dana's; maybe having to remember that phone number at index 1 is not the best idea 
# See next code snippet "Dictionaries as Objects" for the resolution
print("David's Information: ", addressBook["David"])
print("Dana's Phone Number: ", addressBook["Dana"][1])


# #Output is
# David's Information:  ('555 Home St', '4045551234', 'david@david.com')
# Dana's Phone Number:  4045559101