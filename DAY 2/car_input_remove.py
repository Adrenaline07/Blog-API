car_list = ['mazda' , 'honda' , 'nissan']

answer = str(input("Do you want to add or remove: "))
if answer == "add" :
    new_car = str(input("Enter your car model : "))
    car_list.append(new_car)
    print("Updated list is " + str(car_list))
elif answer == "remove" :
    print("Car list: " + str(car_list))
    car_to_remove = str(input("Enter the car to remove: "))
    car_list.remove(car_to_remove)
    print("Updated list is " + str(car_list))
    # THIS IS THE pop OPTION
    # option = int(input("Enter the position of the car you want to remove with 0 as mazda: "))
    # if option == 0 :
    #     car_list.pop(0)
    #     print("Updated list is " + str(car_list))
    # elif option == 1:
    #     car_list.pop(1)
    #     print("Updated list is " + str(car_list))
    # elif option == 2:
    #     car_list.pop(2)
    #     print("Updated list is " + str(car_list))
    # else :
    #     print("Invalid option")
else :
    print("Enter 'add' or 'remove'")

