#To check if a num is even or odd
#asking user input
# we use MODULO

num = int(input("Enter the number to check if it's even or odd: "))
if num%2 == 0 :
    #printing even if the remainder is zero
    print(str(num) + " is an even number")
elif num%2 == 1 :
    print(str(num) + " is an odd number")
else:
    pass
