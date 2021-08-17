show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask User if they have played before
    yes_no = input("Have you played before?").strip().lower()
    if yes_no == "yes" or yes_no == "y":
        print("You chose Yes")
    elif yes_no == "no" or yes_no == "n":
        print("You chose No")
    else:
        print("Please enter Yes or No")
        yes_no = input("Have you played before?").strip().lower()
