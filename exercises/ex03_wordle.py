"""Wordle Game Using While Loops"""

__author__ = "730741513"


def input_guess(secret_word_len: int) -> str:
    """User inputs guess which must be same length as secret word"""

    guess_word: str = input(f"Enter a {secret_word_len} character word: ")

    # Checks if original guess word has differnt length than secret word
    if len(guess_word) != secret_word_len:
        # invalid_guess will keep while loop running until false
        invalid_guess: bool = True

        while invalid_guess:
            guess_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
            # Checks validity of length again
            if len(guess_word) == secret_word_len:
                invalid_guess = False

    return guess_word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Test all indexes of secret_word and checks if it matches char_guess"""
    assert len(char_guess) == 1

    # Declare variables
    index: int = 0
    match: bool = False

    # While loop will go through all characters of secret word
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            match = True
        # This prevents infinite loop
        index += 1

    return match


def emojified(guess: str, secret: str) -> str:
    """This returns the emoji display about the guess accuracy"""
    assert len(guess) == len(secret)

    # Constants
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    # Declare variables
    index: int = 0
    result: str = ""

    while index < len(secret):
        # char_guess must be a single letter
        if contains_char(secret_word=secret, char_guess=guess[index]):
            # If match, checks if the result is in a same or different index
            if secret[index] == guess[index]:
                result += GREEN_BOX
            else:
                result += YELLOW_BOX
        else:
            result += WHITE_BOX

        # incriment index
        index += 1

    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    # Define variables
    turn: int = 1
    continue_game: bool = True
    secret_word_len: int = len(secret)
    guess: int = ""

    while continue_game:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(secret_word_len=secret_word_len)
        print(emojified(guess=guess, secret=secret))

        # Checks win
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            continue_game = False
        # Checks if you went over turn limit, stops loop
        else:
            if turn == 6:
                print("X/6 - Sorry, try again tomorrow!")
                continue_game = False
        # Incriment index
        turn += 1


if __name__ == "__main__":
    main(secret="codes")
