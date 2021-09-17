#fibonacci - 0 1 1 2 3 5 8.......
n=6
a = 0
b = 1
if n < 0: 
    print("Incorrect input") 
elif n == 0: 
    print(a)
elif n == 1: 
    print(a) 
else: 
    for i in range(2,n): 
        c = a + b 
        a = b 
        b = c 
    print(b) 