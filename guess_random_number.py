import random
number_to_ge_guessed = random.randint(0,31)
guess_number = 0
while guess_number != number_to_ge_guessed:
    guess_number = int(input("Select the number between 0 and 30:\n"))
    if guess_number > 0:
        if guess_number > number_to_ge_guessed:
            print("Your number is too large")
        elif guess_number < number_to_ge_guessed:
            print("Your number is too small")
else:
    print("You guessed the number, you won!!!")
