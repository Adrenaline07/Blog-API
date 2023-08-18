class User : 
    def __init__(self, username, password):     #function in a class are called method #init is an initializer/constructor
        self.username = username                #attribute are username, password: Behavior is CONTRIBUTE
        self.password = password                #an object is an instance of a class

    def introduce(self):    #every method inside a class takes self
        print(self.username)

user_1 = User("michael", 1234)
user_2 = User("mike", 3443434)

user_1.introduce()
user_2.introduce()

    
       













