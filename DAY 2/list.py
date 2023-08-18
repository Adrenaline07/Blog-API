# creating list from collection

animals = ['dog' , 'cat' , 'horse' , 'cow', 'sheep']

# # get two varaibles from user and append
# animal_1 = str(input("animal 1 : "))
# animal_2 = str(input("animal 2 : "))

# animals.append(animal_1)    # add elements to the back
# animals.append(animal_2)

# #animals.pop(2) ---> REMOVES BY INDEX
# animals.remove('cow')    #--->REMOVES BY DATA ITSELF

i = 1       #is outside the while loop for any list
while i < len(animals) :            #while i is less than length of list    USING WHILE LOOP
    for animal in animals:          #FOR LOOP inside the WHILE i<len : for each animal in animals
        print(str(i) + ". " + animal)       #print the string of i since i is a number + each animal NOT ANIMALS NOW
        i += 1
#NOTE: this still works when i commented the while loop here
