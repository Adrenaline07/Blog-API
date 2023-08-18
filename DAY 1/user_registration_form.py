    #user to input username, email and age, min age is 17 years
    #u check if the age is greater than 17, u say welcome + username, you can start using the system
    #if age is above 17, user will input location, 

#username = str(input("Enter your username : "))
#email = str(input("Enter email : "))
age = int(input("How old are you : "))

if age > 17 :
    location = str(input("Where are you located: "))
    if location == "lagos" or "ibadan":       #If an if is inside an if, it's called a NESTED if.
        print("User registered successfully")
    elif location == "maiduguri" :
        print("You can register nextweek")
    elif location == "asaba" :
        print("You can register next month")
    else :                          #elif is else if 
        print("Pay $25 to register as your region is not included")
else : 
    print("You are not eligible to register")