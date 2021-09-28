# defining a function to calculate LCM  
def calculate_lcm(h, p):  
    # selecting the greater number  
    if h > p:  
        greater = h  
    else:  
        greater = p  
    while(True):  
        if((greater % h == 0) and (greater % p == 0)):  
            lcm = greater  
            break  
        greater += 1  
    return lcm    
  
# taking input from users  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
# printing the result for the users  
print("The L.C.M. of", num1,"and", num2,"is", calculate_lcm(num1, num2))  
