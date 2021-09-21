# Python program to determine whether
# the number is Armstrong number or not

# Function to calculate x raised to
# the power y
def power(h, p):
	
	if p == 0:
		return 1
	if p % 2 == 0:
		return power(h, p // 2) * power(h, p // 2)
		
	return h * power(h, p // 2) * power(h, p // 2)

# Function to calculate order of the number
def order(h):

	# Variable to store of the number
	n = 0
	while (h != 0):
		n = n + 1
		h = h // 10
		
	return n

# Function to check whether the given
# number is Armstrong number or not
def isArmstrong(h):
	
	n = order(h)
	temp = h
	sum1 = 0
	
	while (temp != 0):
		r = temp % 10
		sum1 = sum1 + power(r, n)
		temp = temp // 10

	# If condition satisfies
	return (sum1 == h)

# Driver code
h = 153
print(isArmstrong(h))

h = 123
print(isArmstrong(h))
