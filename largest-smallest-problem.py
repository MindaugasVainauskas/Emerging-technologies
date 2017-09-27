# 25/09/2017
#Python problem sheet. Problem 6
# Largest and smallest in the list. I am assuming integer numbers since no specific data type was requested

#declare sentinel value
continueLoop = 1

#declare list
numList = []

print("Welcome! This small program will find min and max number in your list")

#run the program until sentinel value is entered
while(continueLoop == 1):
	num = int(input("Enter number to add to the list(-111 to exit): "))
	
	if(num == -111):
		continueLoop = 0  #Sentinel value entered breaks the loop
	else:
		numList.append(num)  #No sentinel value means number is added to the list
	
	
# Following are built in methods to find smallest and largest elements in list
max = max(numList)
min = min(numList)

#print entire list
print("Your entered number list is:")
print(numList)

#Print largest and smallest values
print("Largest number in the list is: %d" % max)
print("Smallest number in the list is: %d" % min)
