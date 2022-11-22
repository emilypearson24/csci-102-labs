# Emily Pearson
# CSCI 102 - section F
# Assessment02B
# References: 
# time: 

# get input
print("Enter your string:")
the_str = str(input("STRING> "))
a = int(input("A> "))
b = int(input("B> "))
c = int(input("C> "))
d = int(input("D> "))

# calculate start and end positions
start_1 = a + 1
start_2 = c + 1

#print slices
print("OUTPUT",the_str[start_1:b],the_str[start_2:d])