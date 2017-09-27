# 27/09/2017
#Python problem sheet. Problem 8
# Merge 2 sorted lists into a single sorted list

#Declare 3 lists to be worked with
listOne = []
listTwo = []
mergedList = []

#Declare sentinel values
sentinel = 1

print("Populate list 1")
#Populate list one
while(sentinel == 1):
	num1 = int(input("Enter number into list 1(-111 to exit): "))
	
	if(num1 == -111):
		sentinel = 0
	else:	
		listOne.append(num1)
		
print("Populate list 2")
#Populate list one
while(sentinel == 0):
	num2 = int(input("Enter number into list 2(-111 to exit): "))
	
	if(num2 == -111):
		sentinel = 1
	else:	
		listTwo.append(num2)

#Sort the lists		
listOne.sort()
listTwo.sort()
print("Lists sorted")
#Print out the lists
print("List 1:")
print(listOne)
print("List 2:")
print(listTwo)

#merge the lists to create new list
mergedList = listOne + listTwo
#sort this new list
mergedList.sort()
print("Sorted merged list")
print(mergedList)