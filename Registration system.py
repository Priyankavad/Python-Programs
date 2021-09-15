try:
    name = input()
    if len(name)<=3:

        raise NameError

    
except NameError:
    print("Invalid Name")

else:
    
    print("Account Created")
