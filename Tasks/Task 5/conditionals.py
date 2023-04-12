# Ask the user for their age
age = int(input("What is your age? "))

# Check if the user is old enough to vote
if age >= 18:
    print("You are old enough to vote!")

    # Ask the user if they want to register to vote
    register = input("Do you want to register to vote? (yes/no) ")

    # If the user wants to register, print a message
    if register.lower() == "yes":
        print("Great, we will help you register to vote.")

    # If the user doesn't want to register, print a message
    elif register.lower() == "no":
        print("Okay, no problem. You can still register later if you change your mind.")

    # If the user enters something else, print an error message
    else:
        print("Sorry, we didn't understand your response. Please enter 'yes' or 'no'.")

# If the user is not old enough to vote, print a message
else:
    print("Sorry, you are not old enough to vote yet. Please come back in a few years!")
