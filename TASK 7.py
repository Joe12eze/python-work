"""
Author : Joe Joseph
Date : 25-10-2024
Discription : Python program to find the largest of three numbers.
 The program should take three numbers as input from the user and determine which one is the largest
"""
number1 = int(input("enter a first number"))
number2 = int(input("enter the second number "))
number3 = int(input("enter the third number"))
if number1>number2 and number1>number3:
    print(number1,"is greater than the other two")
elif number2>number3:
    print(number2,"is greater than the other two")
else:
    print(number3, "is grater than the other two ")
