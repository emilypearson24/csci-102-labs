# Name: Emily Pearson
# CSCI 102 - B
# Assessment 05A
# References: n/a
# Time: 30 mins

#initialize variables
i = ""
num = 0
sum = 0

#prompt
print("Enter values to add. Enter quit when done.")

#while loop
while i != "quit":
  #get input
  i = input("NUMBER> ")
  if i != "quit":
    num += 1
    sum += int(i)
  

#print output
print(f"The addition of the {num} numbers entered is:")
print(f"OUTPUT {num} numbers")
#output sum
print(f"OUTPUT {sum} total")
    
  