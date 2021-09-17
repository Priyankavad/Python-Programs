#GCD of two numbers
m = 10
n = 5
while n!=0:
  r=m%n
  m=n
  n=r
  print("GCD is =",m)
