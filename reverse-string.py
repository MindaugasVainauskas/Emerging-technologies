# 27/09/2017
#Python problem sheet. Problem 10
# Reverse a string and print it out

#Get user to enter the string
print("Enter your string:")
userString = input()

#Reverse the string
reverseString = userString[::-1]  #Using extended slice syntax for a quick way of reversing the string

#Print out reversed string
print("\nYour string reversed is:")
print(reverseString)