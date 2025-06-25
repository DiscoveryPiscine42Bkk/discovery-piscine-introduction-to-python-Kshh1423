#!/usr?bin/env python3
input_password = int(input(" Enter a number less than 25:"))
print(input_password)
if input_password > 25 :
    print("Error")
count = input_password
while count < 25:
    print(f" Inside the loop, my variable is {count}")
    count += 1
