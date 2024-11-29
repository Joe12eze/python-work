"""Author: Joe Joesph
Description:A program that accepts the lengths of three sides of a triangle as inputs.
 The program should output whether or not the triangle is a right triangle .
Implement using functions.
"""
def check_right_triangle(sides):
    sides.sort()
    if sides[2]**2 == sides[0]**2 + sides[1]**2:
            return True
    return False
sides=[]
sides.append(int(input("Enter side 1:")))
sides.append(int(input("Enter side 2:")))
sides.append(int(input("Enter side 3:")))
if check_right_triangle(sides):
    print("The given sides are part of right triangle")
else:
    print("The given sides are not part of right triangle")