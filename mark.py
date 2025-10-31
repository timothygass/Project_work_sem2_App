mark = int(input("Enter student's mark\n"))

if mark >= 80:
    print("Distinction")
elif mark >= 60 and mark < 80:
    print("Merit")
elif mark >= 40 and mark < 60:
    print("Pass")
elif mark< 40:
    print("Failed")