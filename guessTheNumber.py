import random

print("The Number Guessing Game")
print()

# Asking & confirming with user how big of a number they want to guess
while True:
    print()
    digits = input(
        "Enter the size of the number you want to guess - must be between 3 and 8 digits long (bigger numbers are harder to guess):   ")

    if not(digits.isnumeric()):
        print("You didn't enter a number. Try again.")
    else:
        digits = int(digits)
        if 3 <= digits <= 8:
            print()
            print(f"You have chosen {digits} digits.")
            if digits == 3:
                print("You will guess a number between 100 and 999.")
                break
            elif digits == 4:
                print("You will guess a number between 1000 and 9999.")
                break
            elif digits == 5:
                print("You will guess a number between 10,000 and 99,999.")
                break
            elif digits == 6:
                print("You will guess a number between 100,000 and 999,000.")
                break
            elif digits == 7:
                print("You will guess a number between 1,000,000 and 9,999,999.")
                break
            else:
                print("You will guess a number between 10,000,000 and 99,999,999.")
                break
        else:
            print("You did not choose a number between 3 and 8. Try again.")

# rules of the game
print()
print("Now that the computer has its number, here are the rules.")
print("""
1. The first number cannot be a zero.
2. No digit can be repeated. 
For example, the computer would never pick 1231 as the same number - 1 - shows up more than once.
3. You must enter the correct size number in a guess. 
Don't guess 1234 if you wanted the computer to have a 3 digit number.
4. Once you've guessed, the computer will tell you how many numbers are correct and how many numbers are in the correct spot. 
For example, if the number is 123 and you pick 135, the computer will say: You have 2 correct numbers and 1 number in the correct location.
5. Game ends once you've picked the correct number. Good luck!
""")

# computer picks the number - no zero as first digit & no repeats
computer_guess = [0]
while computer_guess[0] == 0:
    computer_guess = random.sample(range(0, 10), digits)

#score & number of tries
score = 200
num_guesses = 0

# user guesses and computer checks against answer
while True:
    print(f"Score:   {score}       Guesses:    {num_guesses}")
    guess = input(
        "Enter your guess:   ")
    if not(guess.isnumeric()):
        print("You didn't enter a number. Try again.")
        continue
    elif len(guess) != digits:
        print("You did not enter a correctly-sized guess. Try again.")
        continue
    else:
        guess = list(guess) #puts string into list of strings
        guess = [int(i) for i in guess] #converts str to int
        if guess == computer_guess:
            computer_guess = [str(i) for i in computer_guess] #converts int to str
            computer_guess = str("".join(computer_guess)) #joins all ints 
            print(
                f"Congrats, you've won! The correct number is {computer_guess}! Great work!!") 
            break
        else:
            #find number of correct digits
            correct_digits = list(i for i in computer_guess if i in guess)
            num_correct_digits = len(correct_digits)
            print(f"You have correctly guessed {num_correct_digits} digits.")
            #find number of digits in correct location
            correct_places = list(i for i, j in zip(computer_guess, guess) if i == j)
            num_correct_places = len(correct_places)
            print(f"You have guessed {num_correct_places} digits in the correct place.")
            print("Try again!")
            score -= 10
            num_guesses += 1