import math
#from math import sqrt,cos,sin  
#line 2 is when you want to specifically import something like cos, tan, sin

#Calculator app for users with access to divide, add, subtract and multiply
username = str(input("Enter your username : "))
#valid_users = ["michael", "victor", "emmanuel"]
#if username  in valid_users :
if username == "joy" or username == "john" or username == "johnson" :
    print("Welcome " + username)
    print("")
    user_age = int(input("Please enter age : "))
    if user_age > 18 :
        operation = input("Enter 'one' for one-word operation and 'two' for two-word operation: ")
        if operation == "two" :
            print("Enter two numbers : ")
            a = float(input("a = "))
            b = float(input("b = "))
            que = input("What operations do you want to perform: 'add', 'sub', 'div', 'mul' : ")
        
            if que == "add" :
                add = str(a + b)
                print("Sum is " + add)
            elif que == "sub" :
                sub = str(a - b)
                print('Subtraction yields ' + sub)
            elif que == "div" :
                div = str(a / b)
                print('Division yields ' + div)
            elif que == "mul":
                mul = str(a * b)
                print("Multiplication yields " + mul)
            else :
                print("not two words")
        elif operation == "one" :
            print("Enter a trig angle: ")
            theta = float(input("theta = "))
            que = input("What operations do you want to perform: 'sin', 'cos', 'tan': ")
            if que == "sin" :
                sinetheta = math.sin(math.radians(theta))
                print("sin " + str(theta) + " = " + str(sinetheta))
            elif que == "cos" :
                costheta = math.cos(math.radians(theta))
                print("cos " + str(theta) + " = " + str(costheta))
            elif que == "tan" :
                tantheta = math.tan(math.radians(theta))
                print("tan " + str(theta) + " = " + str(tantheta))
            else :
                print("error")
        else :
            print("Wrong computation")
    else : 
        print("Sorry, you're not of required age.")    
else :
    print("Your name is not registered in the system")