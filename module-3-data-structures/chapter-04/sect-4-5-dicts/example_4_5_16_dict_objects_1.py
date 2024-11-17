# Dictionaries as Objects > having multiple dictionaries with the same keys but different values
addressBook = {
   "David" : 
      {"address": "555 Home St",
       "phone": "4045551234", 
       "email": "david@david.com"
      },
   "Lucy": 
      {"address": "555 Home St",
       "phone": "404555678", 
       "email": "lucy@lucy.com"
      },
   "Dana":
      {"address": "123 There Rd",
       "phone": "4045559101", 
       "email": "dana@dana.com"
      }
}

print("David's Information: ", addressBook["David"])
print("Dana's Phone Number: ", addressBook["Dana"]["phone"]) # now we can just use the "phone" instead of index 1 like previously


# Output is
# David's Information:  {'address': '555 Home St', 'phone': '4045551234', 'email': 'david@david.com'}
# Dana's Phone Number:  4045559101