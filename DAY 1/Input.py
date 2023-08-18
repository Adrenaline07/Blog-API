#Collect 7 variables, course of study, School, dept
#print, you attend, your dept is, your course is 
username = str(input("Enter a username : ")) 
age = int(input("Age : "))
state_of_origin = str(input("Please, enter your state of origin : "))
#YearOfBirth = int(input("Input your date of birth: "))
calculated_birth_year = 2023 - age

school = str(input("What school do you attend : "))
course = str(input("Enter course of study : "))
faculty = str(input("Faculty : "))

#Code to print username, age, state of origin and birthyear
print("")
print("Welcome " + username + ", You are " + str(age) + " years old." )
print("You are from " + state_of_origin + " and your birthyear is " + str(calculated_birth_year) + ".")
print("Nice, you attend " + school + " and your course of study is " + course + ", faculty of " + faculty + ".")