tax =17.5

item = input("Enter the item description:\n")
price = float(input("Enter the price of the item:\n"))
quantity = int(input("Enter the quantity bought:\n"))


excl_tax_cost = quantity + price
tax_amount = (excl_tax_cost * tax)/100
incl_tax_cost = excl_tax_cost * tax_amount

print("\nThe cost of buying" , quantity , item , "for each is Ghs", incl_tax_cost , 
      "including a tax amount of" ,tax_amount)



