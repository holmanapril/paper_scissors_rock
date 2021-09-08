# Ask user which out of PSR they want to use
user_choice = input("Pick Paper, Scissors or Rock").strip().lower()
print(user_choice)

# Turns specific inputs into different numbers for later use
if user_choice == "rock":
    user_choice = 1
elif user_choice == "paper":
    user_choice = 2
else:
    user_choice = 3

# Prints the updated user_choice to make sure the right number is being printed
print(user_choice)
