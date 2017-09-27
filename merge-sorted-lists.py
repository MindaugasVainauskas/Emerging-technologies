# 27/09/2017
#Python problem sheet. Problem 7
# Merge 2 sorted lists into a single sorted list

#Declare 3 lists to be worked with
listOne = []
listTwo = []
mergedList = []

#Declare sentinel values
sentinel = 1

#Populate list one
while(sentinel == 1):
	num1 = int(input("Enter number into list 1(-111 to exit): "))
	
	if(num1 == -111):
		sentinel = 0
	else:	
		listOne.append(num1)
		
#Populate list one
while(sentinel == 0):
	num2 = int(input("Enter number into list 2(-111 to exit): "))
	
	if(num2 == -111):
		sentinel = 1
	else:	
		listTwo.append(num2)
		
#Print out the lists
print("List 1:")
print(listOne)
print("List 2:")
print(listTwo)