#!/usr/bin/env python3
try :
    p1 = int(input("Pls enter your age :"))
except ValueError :
    print("Pls enter a number")
print(f"You are cureently {p1} years old")
print(f"In 10 years, you will be {p1 + 10} years old")
print(f"In 20 years, you will be {p1 + 20} years old")
print(f"In 30 years, you will be {p1 +30} years old")
