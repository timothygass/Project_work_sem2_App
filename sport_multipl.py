# Initialize counters for each activity
atheletics = 0
swimming = 0
football = 0
badminton = 0

    # Initialize letter variable for the loop
letter = ''  

    # Loop until user enters 'Q' or 'q'
while letter != 'Q' and letter != 'q':
        print("Type in the letter chosen and 'Q' to finish\n\n",
      "A : Atheletics\n",
      "S : Swimming\n",
      "F : Football\n",
      "D : Badminton\n",
      "Q : End Program")

        # Get user input for their choices
        letter = input("Enter your choice: \n")

        # Update the vote counts based on the user's input
        if letter == 'A' or letter == 'a':
            atheletics += 1
        elif letter == 'S' or letter == 's':
            swimming += 1
        elif letter == 'F' or letter == 'f':
            football += 1
        elif letter == 'D' or letter == 'd':
            badminton += 1

    # Print the results
print(f"Atheletics scored",atheletics,"votes")
print(f"Swimming scored",swimming,"votes")
print(f"Football scored",football,"votes")
print(f"Badminton scored ",badminton," votes")