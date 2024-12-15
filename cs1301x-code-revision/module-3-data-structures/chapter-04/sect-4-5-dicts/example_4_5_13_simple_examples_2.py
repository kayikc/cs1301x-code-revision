seatingChart = {"David" :3, "Lucy": 3, "Dana": 2,
                "Addison": 2, "Vrushali": 1, "Bilbo": 3,
                "Sara" :1, "Lugos": 1, "Mireia": 1,
                "Partha": 2, "Venijamin": 1, "Terra": 2,
                "Tryphon": 3, "Gevorg": 1, "Raza": 3,
                "Rein": 3, "Sofia": 2, "Perle": 2
}

# reminder - sep is for between items
# reminder - end is for the end of line of print statement
for (name, table) in seatingChart.items():
   #Print the table for the name
   print(name, " is seated at table #", table, sep="")
   
print()

for i in range(1,4):
   print("The guests at table #", i, " are", sep="", end ="")
   
   for (name, table) in seatingChart.items():
      if i == table:
         print(name, end=" ")
   print()
   
#Output is )
# David is seated at table #3
# Lucy is seated at table #3
# Dana is seated at table #2
# Addison is seated at table #2
# Vrushali is seated at table #1
# Bilbo is seated at table #3
# Sara is seated at table #1
# Lugos is seated at table #1
# Mireia is seated at table #1
# Partha is seated at table #2
# Venijamin is seated at table #1
# Terra is seated at table #2
# Tryphon is seated at table #3
# Gevorg is seated at table #1
# Raza is seated at table #3
# Rein is seated at table #3
# Sofia is seated at table #2
# Perle is seated at table #2

# The guests at table #1 areVrushali Sara Lugos Mireia Venijamin Gevorg
# The guests at table #2 areDana Addison Partha Terra Sofia Perle
# The guests at table #3 areDavid Lucy Bilbo Tryphon Raza Rein