# Emily Pearson
# CSCI 102 - Section F
# Assessment 06A
# References: n/a
# Time: 15 mins

#get input
print("Enter the number to create multiples for.")
num = int(input("NUMBER> "))

print("Enter the maximum index of the list.")
max_index = int(input("INDEX> "))

#create list
multlist = []

#while loop
i = 1
while i <= (max_index + 1):
  multlist.append(num * i)
  i += 1

#print output
print("Your list of multiples is as follows:")
print(f"OUTPUT {multlist}")

print("The first multiple calculated is:")
print(f"OUTPUT {num}")
