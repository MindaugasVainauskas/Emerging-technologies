# 27/09/2017
#Python problem sheet. Problem 7
# Test if String is a palindrome

#define the palindrome test
def isPalindrome(test):
	test = test.lower()  #Put all letters into lowercase
	
	second = reversed(test)
	
	if(list(test) == list(second)):
		print("String is Palindrome")
	else:
		print("String is not a Palindrome!")
	
print("Enter your string:")
checkString = input()

#Run a check if string is Palindrome
isPalindrome(checkString)

