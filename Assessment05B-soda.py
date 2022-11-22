# Emily Pearson
# CSCI 102 - Section
# Assessment 05B
# References:
# Time: 

#get input - empties
print("Enter the number of empty bottles in Blaster's possession at the start of the day.")
empties = int(input("EMPTIES> "))

#get input - found
print("Enter the number of empty bottles that Blaster found during the day.")
found = int(input("FOUND> "))

# update empties
empties += found

# get input - cost 
print("Enter the number of empty soda bottles required to buy a new soda.")
cost = int(input("COST> "))

#initialize variables
drank = 0

# while .....
while empties >= cost:
  #can drink possible sodas per cost
  last = 0
  drank += empties // cost
  last = empties // cost
  empties = last + (empties % cost)

#print output
print("The total number of sodas that Blaster drank is:")
print(f"OUTPUT {drank}")