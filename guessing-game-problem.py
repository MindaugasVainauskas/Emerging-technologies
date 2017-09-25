# 24/09/2017
#Python problem sheet. Problem 5
# Guessing game

import random
import array

#Variables declaration
guessCorrect = 0

#Get maximum random number available for player to guess
maxRandom = int(input("Greetings! Please select maximum positive number to guess from: "))

print("Thank you. This number will be the maximum possible guess.")

#Create random number
randomNumber = random.randint(0, maxRandom)

#create a list to hold guesses
guessList = []

while(guessCorrect == 0):
	guess = int(input("Enter your guess: "))
	
	if(guess > randomNumber):
		print("Your guess is larger than the random number!")
		#finding if element exists is adapted from 
		# https://stackoverflow.com/questions/7571635/fastest-way-to-check-if-a-value-exist-in-a-list
		if guess in guessList:
			continue
		else:
			guessList.append(guess)
	elif(guess < randomNumber):
		print("Your guess is smaller than the random number!")
		if guess in guessList:
			continue
		else:
			guessList.append(guess)
	elif(guess == randomNumber):
		print("Congratulations! Your guessed correctly!")
		if guess in guessList:
			continue
		else:
			guessList.append(guess)
			
		guessCorrect = 1

#Print out the guesses from list
print("Your guesses were:")
print(guessList)
