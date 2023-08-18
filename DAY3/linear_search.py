#function for the linear search
#GOOGLE OWN
def item_search(arr, x):
    for i in range(len(array)):
        if arr[i] == x:
            return i
    return "error"
array = ['D','I','D','N','T','G','E','T','I','T']
print(array)
x = str(input("Input any value to find its index: "))
print("element found at index " + str(item_search(array, x)))



# #COLLINS OWN
# def linear_search(list, target):
#     flag = 0
#     for index in range(len(list)):
#         if list[index] == target:
#             flag = 1
#             print("element found at " + " " + str(index))
#         if flag == 1:
#             pass
#         else : 
#             print("element was not found")

# numbers = [3, 9, 2, 7, 1, 5]
# target_number = 7
