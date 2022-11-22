#Emily Pearson
#CSCI 102 - Section F
#Assessment 07
#References: Used website to understand syntax of 2D arrays (https://snakify.org/en/lessons/two_dimensional_lists_arrays/)
#Time: 45 mins

##create list, append rows into list as elements

#prompt for # row input
print("How many rows does the chessboard have?")
#n = n # of rows input
n = int(input("ROWS> "))
#prompt for column input
print("How many columns does the chessboard have?")
#m = m # of columns input
m = int(input("COLUMNS> "))

#prompt for strings
print("What are the strings with which to pattern it?")
#first = input for first string
first = input("FIRST> ")
#second = input for second string
second = input("SECOND> ")

#create epty list for board
board = []

####FOR LOOPS

# for i range(num rows):
for i in range(n):
  #make new list for each row
  row = []
  
  #if row is even
  if i % 2 ==0:

    #for j in range(num columns):
    for j in range(m):
  
      #if column is even, start with first string
      if j % 2 ==0:
        row.append(first)
      else:
        row.append(second)

        
  #if row is odd
  else:

    #for j in range(num columns):
    for j in range(m):
  
      #if column is even, start w/ second string
      if j % 2 ==0:
        row.append(second)
      else:
        row.append(first)

        
  #append row to board
  board.append(row)


#chessboard description statement
print(f"A chessboard with {n} rows, {m} columns, first string is {first}, and second string is {second} is:")
#output for every rown in board
for i in range(n):
  print(f"OUTPUT {board[i]}")

#2D array output statement
print("And the 2D array representation is:")
print(f"OUTPUT {board}")


  
