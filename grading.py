print("""Choose one of the following:
      

    a for Addition
    s for Substration
    m for Multiplication
    d for Division""")

choice = input().lower()

number1=int(input("Enter the First Number\n"))
number2=int(input("Enter the Second Number\n"))

if choice =="a":
    answer= number1 + number2
elif choice =="s":
    answer= number1 - number2
elif choice =="m":
    answer= number1 * number2
elif choice=="d":
    answer= number1 /number2

print("The result is ", answer)