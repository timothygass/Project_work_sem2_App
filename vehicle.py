vehicle =input("Enter the type of vehicle\n't' for Taxi\n'm' for miniBus\n'c' for Coach\n'o' for okada\n").lower()
                
if vehicle == "t":
    sales = 10 * 4
elif vehicle == "m":
    sales = 7 *15
elif vehicle == "c":
    sales = 100 * 60
elif vehicle == "o":
    sales = 20 * 1
else:
    print("Invalid option")

print("\nThe total sales is", sales)