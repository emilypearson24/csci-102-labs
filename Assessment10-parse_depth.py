#Emily Pearson
#CSCI 102 - Section C
#Assessment 10
#References: https://www.w3schools.com/python/ref_string_split.asp
#Time: 1.5 hours

import csv

#initialize lists
names = []
full = []

#open files
with open("formations.csv","r") as forms:
  with open("formations_parsed.csv","w") as parsed:
    #make reader and writer
    formsReader = csv.reader(forms,delimiter=",")
    next(formsReader)
    parsedWriter = csv.writer(parsed)

    #make list w/ items for each 
    names = ["Depth","Start Depth","End Depth","Difference in Depth","Formation","Age of Formation"]

    #add first line to output file
    parsedWriter.writerow(names)

    ###for loop to go through each line and assign items into names list
    for i in formsReader:
      
      #depth
      depth = i[0]
      
      #split @ hyphen to get start and end
      range = i[0]
      print(range)
      rangeSplit = i[0].split('-')
      #start, make number
      start = float(rangeSplit[0])
      #end, make number
      end = float(rangeSplit[1])

      #difference: make start and end floats
      difference = end - start

      #formation
      form = i[1]

      #age: Paleocene start<700, else Cretaceous
      if float(start) < 700:
        age = "Paleocene"
      else:
        age = "Cretaceous"

      ##append everything into full list
      full.append(depth)
      full.append(start)
      full.append(end)
      #round difference w/ f string
      full.append(f"{difference:.2f}")
      full.append(form)
      full.append(age)

      ##write full list into output file as a row
      parsedWriter.writerow(full)
      
      #reset full list 
      full = []