import random

def provide_hint(number, guess):
    if abs(number - guess) > 50:
        return "You're very cold."
    elif 20 < abs(number - guess) <= 50:
        return "You're cold."
    elif 10 < abs(number - guess) <= 20:
        return "You're warm."
    else:
        return "You're hot!"

x = random.randint(1, 100)
attempts = 0
max_attempts = 10
previous_guesses = set()

while True:
    guess = int(input("Guess a number from 1 to 100: "))
    
    if guess in previous_guesses:
        print("You've already guessed that number. Try again.")
        continue
    else:
        previous_guesses.add(guess)
        attempts += 1

    print("Attempt", attempts, "of", max_attempts)
    if guess < x:
        print("Your guess is too low.")
        print(provide_hint(x, guess))
    elif guess > x:
        print("Your guess is too high.")
        print(provide_hint(x, guess))
    else:
        print("Congratulations! The number is correct.")
        break

    if attempts == max_attempts:
        print("Sorry, you've reached the maximum number of attempts. The number was:", x)
        break

    print()
