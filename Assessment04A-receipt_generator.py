# Emily Pearson
# CSCI 102 - Section
# Assessment 04A
# References: n/a
# Time: 20 mins

#get input
comp_name = input("Enter company name: ")
comp_loc = input("Enter company city/state: ")
cash_name = input("Enter cashier name: ")
name1 = input("Purchased item 1 name: ")
price1 = float(input("Purchased item 1 price: "))
name2 = input("Purchased item 2 name: ")
price2 = float(input("Purchased item 2 price: "))
name3 = input("Purchased item 3 name: ")
price3 = float(input("Purchased item 3 price: "))
end_msg = input("Enter your favorite ending message: ")

#print
print("")
print("        RECEIPT GENERATOR")
print("-----------------------------------")
print(f'    {comp_name}')
print(f'    {comp_loc}')
print("===================================") 
print("    Welcome Valued Customer")
print("===================================")
print('    Item Name       Item Price')
print(f'    {name1}        ${price1:.2f}')
print(f'    {name2}        ${price2:.2f}')
print(f'    {name3}        ${price3:.2f}')
print("===================================")
print(f'    Total Cost of Order: {(price1 + price2 + price3):.2f}')
print("===================================")
print(f'    {end_msg}')
print("-----------------------------------")