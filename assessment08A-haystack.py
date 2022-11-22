#Emily Pearson
#CSCI 102 – Section F
#Assessment 08B
#References: 
#Time: 

#get string 1
print("Enter a DNA string S:")
s = input("S> ")

#get string 2
print("Enter a substring T:")
t = input("T> ")

#input errors
if len(t) > len(s):
  print("Error: Substring is longer than DNA string")
  print("OUTPUT ERROR")

#split up string to find substring
count = 0
index = [1,3,4]


#print output
print(f"The total number of substrings found is {count}")
print(f"OUTPUT {count}")
print(f"The starting indices of these substrings in S are: {index}")
print(f"OUTPUT {index}")