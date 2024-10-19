"""Author : Joe Joseph
 Date:19-10-2024
 Description :Python program that performs the following tasks:
 Create, concatenate, and print a string and access a sub-string from a given string."""

str1=input("Enter the your name:")
str2=input("Enter the last string:")
result=str1+" "+str2
print(result)
l=len(str1)
print(l)
last_str=result[:l]
print(last_str)

