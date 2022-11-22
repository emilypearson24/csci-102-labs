#Emily Pearson
#CSCI 102  Section F
#assessment 11
#references: https://docs.python.org/3/library/math.html for math library functions, TA James explained that i don't need to use input statements and that I can call function inside of function definitions
#time: 45 mins

import math

#print_output: get input from user, fstring to print input after OUTPUT
def print_output(instring):
  print(f"OUTPUT {instring}")
  return


#cylinder_vol: function have to argument things, get 2 inputs, make inputs floats, calc volume, fstring print rounded 2 dec places
def cylinder_vol(radius,height):
  vol = 3.1415 * radius**2 * height
  print_output(f"{vol:.2f}")
  return

#lbs_to_kg: 
def lbs_to_kg(lbs):
  kg = lbs * 0.4536
  print_output(f"{kg:.4f}")
  return

#polar_coords
def polar_coords(x,y):
  r = math.sqrt(x**2 + y**2)
  theta = math.atan2(y,x)
  theta *= 180/3.1415
  print_output(f"r: {r:.2f}")
  print_output(f"theta: {theta:.2f}")
  return

#yen to dollars
def yen_to_dollars(yen):
  dollars = yen * 0.0068
  print_output(f"{dollars:.2f}")
  return

#quadratic form: print smaller root first
def quad_form(a,b,c):
  quad1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
  quad2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
  if quad1 < quad2:
    print_output(f"{quad1:.0f}")
    print_output(f"{quad2:.0f}")
  else:
    print_output(f"{quad2:.0f}")
    print_output(f"{quad1:.0f}")  
  return