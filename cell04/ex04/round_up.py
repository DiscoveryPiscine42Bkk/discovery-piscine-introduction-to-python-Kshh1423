#!/usr/bin/env python3
try :
      num_1 =  float(input("Gimme a number : "))
except ValueError :
      print("Pls enter an integer or a decimal")
print(round(num_1))
