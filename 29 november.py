"""Author: Joe Joesph
Description:Program to check whether the given number is a valid mobile number or not using functions.

Rules:

    Every number should contain exactly 10 digits.
    The first digit should be 7 or 8 or 9
"""
def mobile_number (num):
    if len(num)==10 and num[0] in "789":
        print( "Valid phone number")
    else :
        print("Invalid phone number")

mobile_number ('544635447')