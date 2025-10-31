income_tax =20

name = str(input("Enter the employees name\n"))
hours_worked = float(input("Enter the hour worked\n"))
pay_per_hour = float(input("Enter the pay per hour\n"))


gross_pay = hours_worked * pay_per_hour
income_tax_amount = gross_pay * income_tax/100
net_pay = gross_pay - income_tax_amount

print(name, ",\nGross Pay = Ghs", gross_pay, "income Tax = Ghs", income_tax_amount, 
      "Net Pay = Ghs", net_pay)
