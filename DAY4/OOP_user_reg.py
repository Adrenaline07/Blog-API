
# Define a class to represent user registration
class UserRegistration:
    def __init__(self, username, password, fullname, location, state_of_origin, date_of_birth):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.location = location
        self.state_of_origin = state_of_origin
        self.date_of_birth = date_of_birth

# Create an empty list to store user information
user_list = []

# Collect the number of users to register
num_users = int(input("___Enter the number of users to register: ___"))
for i in range(num_users):
    print("___Enter user information: ___")
    username = input("Username: ")
    password = input("Password: ")
    fullname = input("Full Name: ")
    location = input("Location: ")
    state_of_origin = input("State of Origin: ")
    date_of_birth = input("Date of Birth: ")

    # This is the instance of the UserRegistration class and append it to the list
    user = UserRegistration(username, password, fullname, location, state_of_origin, date_of_birth)
    user_list.append(user)  
    #append the user to empty user list
    print("User registered successfully!\n")

# Display the registered users' information
print("___Registered Users: ___")
index = 1
while index <= len(user_list):
    user = user_list[index - 1]
    print(f"User {index}:")
    print("Username:", user.username)
    print("Full Name:", user.fullname)
    print("Location:", user.location)
    print("State of Origin:", user.state_of_origin)
    print("Date of Birth:", user.date_of_birth)
    print()
    index += 1

#This assignment is done with external but i have learnt something new
