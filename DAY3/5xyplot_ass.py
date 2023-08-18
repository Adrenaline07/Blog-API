import matplotlib.pyplot as graph

print("---Graph to print 5 coordinates---")
print("Enter values x1 & y1 up to x5 & y5")
# User will input 5 coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
x3 = float(input("Enter x3: "))
y3 = float(input("Enter y3: "))
x4 = float(input("Enter x4: "))
y4 = float(input("Enter y4: "))
x5 = float(input("Enter x5: "))
y5 = float(input("Enter y5: "))

x = [x1, x2, x3, x4, x5]
y = [y1, y2, y3, y4, y5]
#Appemding x values
x.append(x1)
x.append(x2)
x.append(x3)
x.append(x4)
x.append(x5)
#Appending y values
y.append(y1)
y.append(y2)
y.append(y3)
y.append(y4)
y.append(y5)
#printing x & y list
print("X = " + str(x))
print("Y = " + str(y))

graph.plot(x,y) #plotting the points
# labeling the AXES
graph.xlabel('x - axis') 
graph.ylabel('y - axis') 
#graph title
graph.title('My first graph')
graph.show()


