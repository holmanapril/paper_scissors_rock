# Functions
def chosen_symbol(question):
    valid = False
    while not valid:
        user_choice = input(question).strip().lower()
        if user_choice == "rock":
            user_choice = 1
            return user_choice
        elif user_choice == "paper":
            user_choice = 2
            return user_choice
        elif user_choice == "scissors":
            user_choice = 3
            return user_choice
        else:
            print("<error>")


# Main Routine
user_input = chosen_symbol("Please choose either paper scissors or rock")
print(user_input)
