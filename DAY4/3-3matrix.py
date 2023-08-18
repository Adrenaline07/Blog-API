# Set the dimensions of the matrix
rows = 3
cols = 3

# Create an empty list to store the matrix
matrix = []

# Loop through each row
for i in range(rows):
    row = []  # Create an empty list for each row
    for j in range(cols):
        # Prompt the user to input a value for the current element
        value = float(input("Enter value for row " + str(i + 1) + ", column " + str(j + 1) + ": "))
        row.append(value)  # Add the value to the current row
    matrix.append(row)  # Add the current row to the matrix

# Display the entered matrix
print("\nYou entered the following matrix:")
for row in matrix:
    print(row)  # Print each row of the matrix
