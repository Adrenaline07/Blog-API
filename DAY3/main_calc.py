from functions_maincalc import *

username = str(input("Enter your username : "))

print("Welcome " + username)
print("")

operation = int(input("Enter 1 for:'add','sub','div','mul' and 2 for: 'sin' 'tan' 'cos' 'sqrt' : "))
if operation == 1:
    task = str(input("Enter 'add','sub','div','mul' for operation to be performed: "))
    num1 = int(input("Enter 1st no:"))
    num2 = int(input("Enter 2nd no: "))
    if task == "add" :
        add(num1, num2)
    elif task == "sub":
        sub(num1, num2)
    elif task == "mul":
        mul(num1, num2)
    elif task == "div":
        div(num1, num2)
    else:
        print("Choose valid operation")
elif operation == 2:
    task = str(input("Enter 'sin' 'tan' 'cos' 'sqrt' for operation to be performed: "))
    num = float(input("Input your value: "))
    if task == "sin" :
        sin(num)
    elif task == "cos" :
        cos(num)
    elif task == "tan" :
        tan(num)
    elif task == "sqrt" :   
        sqrt(num)
    else:
        print("input error")
else:
    print("You have not chosen an option")