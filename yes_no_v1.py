# Ask User if they have played before
yes_no = input("Have you played before?").strip().lower()
if yes_no == "yes":
    print("You chose Yes")
elif yes_no == "y":
    print("You chose Yes")
elif yes_no == "no":
    print("You chose No")
elif yes_no == "n":
    print("You chose No")
else:
    print("Please enter Yes or No")
    yes_no = input("Have you played before?").strip().lower()
