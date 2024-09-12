"""EX02- Chardle Game"""

__author__ = "730741513"


def input_word() -> str:
    """Gathers word input from user"""
    user_word: str = input("Enter a 5-character word: ")
    # Function will only accept 5 letter words without error
    if len(user_word) != 5:
        print("Error: Word must contain 5 characters")
        exit()  # Exit function due to error
    return user_word


def input_letter() -> str:
    """Gathers letter input from user"""
    user_letter: str = input("Enter a single character: ")
    # Function only accepts 1 letter
    if len(user_letter) != 1:
        print("Error: Character must be a single character.")
        exit()  # Exit function due to error
    return user_letter


def contains_char(word: str, letter: str) -> None:
    """Checks it user_letter matches any letters in user_word"""
    # Total num of matches between letter and word initialized
    match_count: int = 0

    print("Searching for " + letter + " in " + word)
    # Prints when letter is found as specific index of word
    # Use if statments because many can be true stimataneously
    if letter == word[0]:
        print(letter + " found at index 0")
        match_count = match_count + 1
    if letter == word[1]:
        print(letter + " found at index 1")
        match_count = match_count + 1
    if letter == word[2]:
        print(letter + " found at index 2")
        match_count = match_count + 1
    if letter == word[3]:
        print(letter + " found at index 3")
        match_count = match_count + 1
    if letter == word[4]:
        print(letter + " found at index 4")
        match_count = match_count + 1

    # Prints instances of letter in word for 0, 1, and 2+ matches
    if match_count == 0:
        print("No instances of " + letter + " found in " + word)
    elif match_count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:  # For multiple matches
        print(str(match_count) + " instances of " + letter + " found in " + word)


def main() -> None:
    """Puts whole program together"""
    # Function call
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
