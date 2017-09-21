# 21/09/2017
#Python problem sheet. Problem 3
# Fizzbuzz

#for loop
for i in range(1, 100):
#check multi-condition statement first or it wont get printed.(I tried)
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	elif i % 3 == 0:
		print("fizz")
	elif i % 5 == 0:
		print("buzz")
	else:
	#if none of above are true simply output current index number
		print(i)