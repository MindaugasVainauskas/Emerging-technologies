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
print("Factorial of your number: %d" % factorised)

#convert number into string
factorised_string = str(factorised)

#declare sum at 0
sum = 0

#Calculate sum of digits by grabbing character from string, converting to int and adding to sum.
for i in factorised_string:
	sum += int(i)
	
#print the sum of digits	
print("Digit sum for number is: %d" % sum)