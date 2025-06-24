#!/usr/bin/env python3
#type only integers
p1 = int(input("enter the first number:"))
p2 = int(input("Enter the second number:"))
p3 = (p1 * p2)
print(f"{p1} x {p2} = {p3}")
if p3 > 0 :
    print("Result is positive")
elif p3 < 0 :
    print("The result is negative")
else :
    print("The result is zero")
