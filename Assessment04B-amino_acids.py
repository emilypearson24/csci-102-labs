# Emily Pearson
# CSCI 102 - Section
# Assessment 04B
# References: n/a
# Time: 

# get input
print("Input the chemical elements of the amino acid:")
c = int(input("CARBON>"))
h = int(input("HYDROGEN>"))
n = int(input("NITROGEN>"))
o = int(input("OXYGEN>"))
s = int(input("SULFUR>"))
acid = ""

# if c==3, alanine or cysteine
if c == 3:
  if s == 0:
    acid = "Alanine"
  else:
    acid = "Cysteine"

# if c==6, arganine or histidine
elif c == 6:
  if h == 14:
    acid = "Arginine"
  else:
    acid = "Histidine"

# if c==4, asparagine
elif c == 4:
  acid = "Asparagine"
else:
  acid = "Glutamine"

#print output
print(f'The amino acid for {c}C--{h}H--{n}N--{o}O--{s}S is {acid}')
print(f'OUTPUT {c}C--{h}H--{n}N--{o}O--{s}S')
print(f'OUTPUT {acid}')