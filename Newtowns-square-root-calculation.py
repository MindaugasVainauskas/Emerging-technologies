#21/09/2017
#Lab 1
#Calculating Newton's method for square roots

x = 20

z_next = lambda z: (z - ((z*z - x) / (2 * x)))

current = 1.0

while current != z_next(current):
	print("Current guess: %0.10f" % (current))
	current = z_next(current)