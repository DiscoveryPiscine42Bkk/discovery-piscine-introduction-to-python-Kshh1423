#!/usr/bin/env python3
try :
      num_1 =  float(input("Gimme a number : "))
except ValueError :
      print("Pls enter an integer or a decimal")
print(num_1)
if num_1 .is_integer() :
      print("This number is an integer")
else:
      print("This number is decmial")
