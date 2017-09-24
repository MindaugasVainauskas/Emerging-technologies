# 24/09/2017
#Python problem sheet. Problem 5
# Guessing game

import random

#Variables declaration
guessCorrect = 0

#Get maximum random number available for player to guess
maxRandom = int(input("Greetings! Please select maximum number to guess from: "))

print("Thank you. This number will be the maximum possible guess.")

#Create random number
randomNumber = random.randint(0, maxRandom)

while(guessCorrect == 0):
	guess = int(input("Enter your guess: "))
	
	if(guess > randomNumber):
		print("Your guess is larger than the random number!")
	elif(guess < randomNumber):
		print("Your guess is smaller than the random number!")
	elif(guess == randomNumber):
		print("Congratulations! Your guessed correctly!")
		guessCorrect = 1

