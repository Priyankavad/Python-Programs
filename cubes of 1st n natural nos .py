# Simple Python program to find sum of series
# with cubes of first n natural numbers

# Returns the sum of series
def sumOfSeries(n):
	hp = 0
	for i in range(1, n+1):
		hp +=i*i*i
		
	return hp


# Driver Function
n = 5
print(sumOfSeries(n))

# Code Contributed by Mohit Gupta_OMG <(0_o)>
