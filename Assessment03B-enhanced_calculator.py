# Emily Pearson
# CSCI 102 - Section 
# Assessment 03B
# References: n/a
# Time: 

#create/initialize variable
op1 = 0.0
op2 = 0.0
sum = 0.0
difference = 0.0
quotient = 0.0
product = 0.0
remainder = 0.0

#get input for operands
print("Input the first operand.")
op1 = float(input("FIRST>"))
op2 = float(input("SECOND>"))

#get input for operation
print("Choose one of the following operations:\n  1 - addition\n  2 - subtraction\n  3 - multiplication\n  4 - division")
op = int(input("OPERATION>"))

#sum
sum = op1 + op2

#difference
difference = op1 - op2

#product
product = op1 * op2

#integer division
quotient = op1 // op2

#remainder - modulus
remainder = op1 % op2


#rounding
sum = f'{sum:.6f}'
difference = f'{difference:.6f}'
product = f'{product:.6f}'
quotient = f'{quotient:.0f}'
remainder = f'{remainder:.0f}'


#blank line
print("")

#printing if elses
if op == 1:
  print("OUTPUT",sum)

if op == 2:
  print("OUTPUT",difference)

if op == 3:
  print("OUTPUT",product)

if op == 4:
  print("OUTPUT",quotient)
  print("OUTPUT",remainder)

print("Thank you for using our calculator.")