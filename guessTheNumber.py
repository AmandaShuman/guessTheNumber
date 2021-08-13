print("The Number Guessing Game")
while True:
    print()
    digits = input("Enter the size of the number you want to guess - must be between 3 and 8 digits long:   ")

    if (not(digits.isnumeric())):
        print("You didn't enter a number. Try again.")
    else:
        digits = int(digits)
        if (3 <= digits <= 8):
            print(f"You have chosen to guess a random number that contains {digits} digits long.")
            break
        else:
            print("You did not choose a number between 3 and 8. Try again.")
            continue
