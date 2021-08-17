# Functions
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).strip().lower()
        if response == "yes" or yes_no == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please enter Yes or No")


# Main Routine
show_instructions = yes_no("Have you played the game before? ")
print("You chose {}".format(show_instructions))
