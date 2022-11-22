# Emily Pearson
# CSCI 102 - Section F
# Assessment 06B
# References:
# Time: 

#get count input
print("Count of numbers to estimate:")
count = int(input("COUNT> "))


#initialize lists and variables
numlist = []
bg = ""
itlist = []
ans = ""
outlist = []


#get input for count # of numbers
for i in range(count):
  
  innum = float(input("NUMBER> "))
  numlist.append(innum)


#estimate sqrt for count # of numbers
for i in range(0,count):

  #initialize ig
  ig = 10

  #calculate first iteration of bg, initialize iterations
  bg = (ig + numlist[i]/ ig) / 2
  iter = 1

  #if ig == bg then set bg to answer, append answer to outlist, append iterations to itlist
  if ig == bg:
    ans = ig
    outlist.append(ans)
    itlist.append(iter)

  #else enter while loop  
  else:
    
    #while ig != bg, go through equation and set ig = bg
    while ig != bg:
      
      #apply formula for bg
      ig = (ig + numlist[i]/ ig) / 2
      bg = (ig + numlist[i]/ ig) / 2

      #add to iterations variable
      iter += 1

      #if ig == bg then set bg to answer, add 1 to iterations append answer to outlist, append iterations to itlist; else repeat while loop
      if ig == bg:
        
        ans = bg
        outlist.append(ans)
        itlist.append(iter)

#print outputs
print("The square roots are as follows:")

#for loop to go through items in lists, round in f-string
for i in range(0,count):
  print(f"OUTPUT After {itlist[i]} iterations, {float(numlist[i]):.1f}^0.5 = {float(outlist[i]):.2f}")

      

        
    
    
  