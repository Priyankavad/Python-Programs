import cmath  
h = float(input('Enter a: '))  
p = float(input('Enter b: '))  
n = float(input('Enter c: '))  
  
# calculate the discriminant  
m = (p**2) - (4*h*n)  
  
# find two solutions  
sol1 = (-p-cmath.sqrt(m))/(2*h)  
sol2 = (-p+cmath.sqrt(m))/(2*h)  
print('The solution are {0} and {1}'.format(sol1,sol2)) 
