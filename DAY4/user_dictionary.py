users = [] #empty list

username = str(input("Enter username: "))
password = input("Enter password: ")

user = {        #this is a dictionary
    "username" : username,
    "password" : password
}

users.append(user)  #this appends the entered input to the dictionary
print(users)