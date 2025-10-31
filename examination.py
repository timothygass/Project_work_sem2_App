sum1 = 0  # Sum for first exam
sum2 = 0  # Sum for second exam
sum3 = 0  # Sum for third exam
counter = int(input("Enter the number of students: "))  # Get the number of students
    
    # Validate the number of students
while counter < 1 or counter > 50:
        print("Error! The number of students must be between 1 and 50.")
        counter = int(input("Please re-enter the number of students: "))
    
    # Iterate over each student
for n in range(counter):
        student_id = input("Enter Student's ID: ")
        name = input("Enter Student's Name: ")
        print(f"Enter the three exam marks for {name}:")
        
        # Get the exam marks (convert input to integers)
        exam1 = int(input("First exam: "))
        exam2 = int(input("Second exam: "))
        exam3 = int(input("Third exam: "))
        
        # Update the sums
        sum1 += exam1
        sum2 += exam2
        sum3 += exam3
        
        # Calculate the average for this student
        average_student = (exam1 + exam2 + exam3) / 3
        
        # Determine the grade based on the average
        if average_student < 30:
            grade = "Fail"
        elif average_student < 40:
            grade = "Referral"
        elif average_student < 60:
            grade = "Pass"
        elif average_student < 75:
            grade = "Merit"
        else:
            grade = "Distinction"
        
        # Print the student's results
        print(f"Student ID: {student_id}")
        print(f"Name: {name}")
        print(f"First exam: {exam1}")
        print(f"Second exam: {exam2}")
        print(f"Third exam: {exam3}")
        print(f"{name}, your average is: {average_student:.2f}")
        print(f"Your grade is: {grade}")
        print("------------------------------")
    
    # Calculate the averages for each exam
average_exam1 = sum1 / counter
average_exam2 = sum2 / counter
average_exam3 = sum3 / counter
    
    # Calculate the overall class average
average_class = (sum1 + sum2 + sum3) / (3 * counter)
    
    # Print the class averages
print("\nOverall Averages:")
print(f"Exam 1 average: {average_exam1:.2f}")
print(f"Exam 2 average: {average_exam2:.2f}")
print(f"Exam 3 average: {average_exam3:.2f}")
print(f"Class average: {average_class:.2f}")