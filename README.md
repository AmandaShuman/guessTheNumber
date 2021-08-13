# guessTheNumber

## About me & why this program
I'm a mathematician and a former math teacher and this game used to be one of my students' favorites if we had free time in class. The idea is that students need to guess a number picked out in advance by the teacher (or in this case, computer). 

## The rules
First, the students (user) need to tell the teacher how many digits of the number is they want to guess. The teacher then has to choose the number. Some rules we implemented - all digits 0 - 9 can be used, but there cannot be any repeated digits.

From there, the students will guess the number. This is where the fun comes in. Once the students provide their guess, the teacher will write their guess on the board and tell them 2 things:
1. How many digits are correct, and 
2. How many digits are in the correct spot.

## example
Let's say the students say, "we want a 5 digit number," so the teacher picks the number 34879 (but doesn't tell the students what the number is).

To continue with the example, let's say the students pick the number 48209. The teacher would write the number on the board and tell them:
1. 3 numbers are correct and 
2. 1 number is in the correct location.

## When does it end???
The game would continue with students guessing the number until they get all the digits correct and in the correct order. Then the teacher will say something along the lines of, "Congrats, you've won!" or something similar.

## skills learned
1. Using the zip() function to compare lists in order for equal strings/integers.
2. Checking that a string has all numbers or not using isnumeric() function.
3. random.sample() function to get a unique list
4. Running a while loop to make sure the first number in my list was not a zero.
5. Using len() function to get the length of a list
6. Using list() function to change a string into a list of characters.
7. Using int(i) for i in listA to change a list of strings into a list of integers.
8. Using str(i) for i in listA to change a list of integers into a list of strings.
9. Using join() function to join all elements of list together into one.