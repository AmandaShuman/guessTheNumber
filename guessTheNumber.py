print("The Number Guessing Game")
while True:
    print()
    digits = input("Enter the size of the number you want to guess - must be between 3 and 8 digits long (bigger numbers are harder to guess):   ")

    if (not(digits.isnumeric())):
        print("You didn't enter a number. Try again.")
    else:
        digits = int(digits)
        if (3 <= digits <= 8):
            #add specific cases for 3 - 8 to make it easier for user to see between what numbers they need to guess.
            print(f"You have chosen to guess a random number that contains {digits} digits.")
            break
        else:
            print("You did not choose a number between 3 and 8. Try again.")

#rules of the game
print("""
Now that the computer has its number, here are the rules.
1. The first number cannot be a zero.
2. No digit can be repeated. 
For example, the computer would never pick 1221 or 1231 as the same number shows up more than once.
3. You must enter the correct size number in a guess. 
Don't guess 1234 if you wanted the computer to have a 3 digit number.
4. Once you've guessed, the computer will tell you how many numbers are correct and how many numbers are in the correct spot. 
For example, if the number is 123 and you pick 135, the computer will say: You have 2 correct numbers and 1 number in the correct location.
5. Game ends once you've picked the correct number. Good luck!
""")
