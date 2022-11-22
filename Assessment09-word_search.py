#Emily Pearson
#CSCI 102 - Section C
#Assessment 09
#references ZyBooks ch. 21
#time: 1.5 hrs

#import random library
import random

#open file
with open("dictionary.txt","r") as f:
  
  #get input
  print("Enter the length of the words to find:")
  length = int(input("LENGTH> "))
  print("Enter the seed to use:")
  seed = input("SEED> ")

  #create list of all words
  dictlist = f.readlines()
  
  #initialize word count variable
  count = 0

  #initialize list of words w/ correct length
  oflength = []

  
  #find words w/ correct length 
  for i in range(len(dictlist)):

    #if a word is the correct length
    ############length-1 bc ????
    if len(dictlist[i]) - 1 == length:
      
      #add to counter variable
      count += 1
      
      #append to list
      oflength.append(dictlist[i])
      
      
  #go to output if no words of length, if only not then get random word
  if count == 0:

    #print output
    print(f"The number of words with length {length} is:")
    print(f"OUTPUT {count}")
    print(f"There are no words of length {length} in the dictionary.")
    print(f"OUTPUT None")

  #else, get random word
  else:
    
    #seed RNG
    random.seed(seed)
  
    #get random index in oflength list
    randnum = random.randint(0,len(oflength)-1)

    #get word from randnum index in oflength list
    randword = oflength[randnum]


  #print output based on count
  if count == 1:

    print(f"The number of words with length {length} is:")
    print(f"OUTPUT {count}")
    print(f"Here is the only word with length {length}:")
    print(f"OUTPUT {randword}")

  if count > 1:
    print(f"The number of words with length {length} is:")
    print(f"OUTPUT {count}")
    print(f"Here is a random word with length {length}:")
    print(f"OUTPUT {randword}")