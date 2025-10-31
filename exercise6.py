# Declaring the empty list
I = []
# Number of elements will be entered by the user
n = int(input("Enter the number of elements in the list:"))

# for loop to take the input
for i in range(0,n):
    # The input is taken from the user and added to the list as the item
    I.append(input("Enter the item:"))
    print("printing the list items:")

    # traversal loop to print the items
    for i in I:
        print(i, end =" ")
