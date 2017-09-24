# 24/09/2017
#Python problem sheet. Problem 4
# Factorial digit sum

#import the library to use factorial function
import math

#ask for a number to input
factNum = int(input("Enter the number for a factorial: "))

print("You entered %d" % factNum)

#Calculate the factorial of number
factorised = math.factorial(factNum)
print("Here is a factorial of your number: %d" % factorised)