name = input("Enter the name of the salesman\n")
years = float(input("Enter the number of years served\n"))
sales = float(input("Enter the sales figures\n"))

wage = sales * 15/100

if years > 3:
    bonus = wage *10/100
else:
    bonus = 0

wage = wage + bonus

print(name, ", has sales figures of Ghs", sales, "a bonus of Ghs",bonus, "and Ghs", wage, "wages") 