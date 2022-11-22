# Emily Pearson
# CSCI 102 – Section F 
# Assessment 02A
# References: TA James D helped me fix my errors, Eric helped me to understand the assignment
# Time: 60 mins

#float-> math-> round ->print
#1-3: 1 decimal
#4: integer 
#5: 2 decimals
#quotient: integer division
#:.0f

#create/initialize variable
op1 = 0.0
op2 = 0.0
sum = 0.0
difference = 0.0
quotient = 0.0
product = 0.0
remainder = 0.0

#get input
print("Input the first operand.")
op1 = float(input("FIRST>"))
op2 = float(input("SECOND>"))

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
sum = f'{sum:.1f}'
difference = f'{difference:.1f}'
product = f'{product:.1f}'
quotient = f'{quotient:.0f}'
remainder = f'{remainder:.2f}'


#printing
print("")
print(f'The sum of {op1} and {op2} is {sum}')
print("OUTPUT",sum)

print(f'The difference of {op1} and {op2} is {difference}')
print("OUTPUT",difference)

print(f'The product of {op1} and {op2} is {product}')
print("OUTPUT",product)

print(f'The quotient of {op1} and {op2} is {quotient}')
print("OUTPUT",quotient)

print(f'The remainder of {op1} and {op2} is {remainder}')
print("OUTPUT",remainder)