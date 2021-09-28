# defining a function to calculate HCF  
def calculate_hcf(h, p):  
    # selecting the smaller number  
    if h > p:  
        smaller = p  
    else:  
        smaller = h  
    for i in range(1,smaller + 1):  
        if((h % i == 0) and (p % i == 0)):  
            hcf = i  
    return hcf  
  
# taking input from users  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
# printing the result for the users  
print("The H.C.F. of", num1,"and", num2,"is", calculate_hcf(num1, num2))  
