# 27/09/2017
#Python problem sheet. Problem 7
# Test if String is a palindrome

#define the palindrome test
def isPalindrome(test):
	test = test.lower()  #Put all letters into lowercase
	
#Following is adapted from:
# https://www.programiz.com/python-programming/examples/palindrome	
	
	second = reversed(test) #Temporary string is a reversed version of test string
	
	if(list(test) == list(second)):
		print("String is Palindrome")
	else:
		print("String is not a Palindrome!")
	
#Get user to enter the string
print("Enter your string:")
checkString = input()

#Run a check if string is Palindrome
isPalindrome(checkString)

