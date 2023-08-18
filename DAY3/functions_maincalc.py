# functions in the calculator to be imported to the main file
import math
#add
def add(a, b): #this defines a function named 'add' that takes two argument 'a' and 'b' 
    add  = a + b
    print(print("Sum is " + str(add)))

def sub(a, b):
    sub = a - b
    print('Subtraction yields ' + str(sub))

def div(a,b):
    div = a/b
    print('Division yields ' + str(div))

def mul(a,b):
    mul = a * b
    print("Multiplication yields " + str(mul))

def sin(theta):
    sin = math.sin(math.radians(theta))
    print("sin " + str(theta) + " = " + str(sin))

def cos(theta):
    cos = math.cos(math.radians(theta))
    print("cos " + str(theta) + " = " + str(cos))

def tan(theta):
    tan = math.tan(math.radians(theta))
    print("tan " + str(theta) + " = " + str(tan))

def sqrt(theta):
    sqrt = math.sqrt(theta)
    print("Value of sqrt is " + str(sqrt))
    
