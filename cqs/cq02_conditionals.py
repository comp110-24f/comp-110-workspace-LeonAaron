"""Number guseeing game"""

__author__ = "730741513"


def guess_a_number() -> None:
    """Function to guess a number"""
    secret: int = 7
    guess: str = input("Guess a number: ")  # Number that user guesses
    print("Your guess was " + guess)
    # Shows it guess was right, too low, or too high bu comparing secret and guess
    if int(guess) == secret:  # Changed guess to int to compare correctly
        print("You got it!")
    elif int(guess) < secret:  # Changed secret to string for proper concatenation
        print("Your guess was too low! The secret number is " + str(secret))
    elif int(guess) > secret:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
