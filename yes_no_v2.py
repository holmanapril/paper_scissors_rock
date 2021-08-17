show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask User if they have played before
    yes_no = input("Have you played before?").strip().lower()
    if yes_no == "yes" or yes_no == "y":
        yes_no = "yes"
        print("Program Continues")
    elif yes_no == "no" or yes_no == "n":
        yes_no = "no"
        print("Display Instructions")
    else:
        print("Please enter Yes or No")
