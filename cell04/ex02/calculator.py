#!/usr/bin/env python3
try :
    num_1 = int(input(" Give me the first number:"))
    num_2 = int(input("Give me the second number:"))
    print( num_1 )
    print( num_2 )
    print("Thank you!")
except ValueError :
    print("Pls enter numbers and try again")
print(F"{num_1} + {num_2} = {num_1 + num_2}")
print(f"{num_1} - {num_2} = {num_1 - num_2}")
print(f"{num_1} / {num_2} = {num_1 / num_2}")
print(f"{num_1} x {num_2} = {num_1 * num_2}")
