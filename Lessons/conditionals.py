"""Practice with conditoinals"""


def less_than_10(num: int) -> None:
    """Tell me if num is < 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("small number")
    else:
        print("big number")
    print("Have a nice day")


def should_i_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger"""
    if hungry:  # Conditional expression
        print("eat some food")
    else:
        print("Don't eat")  # "else block"
    print("Good job")  # Alyawys exectes


def check_first_letter(word: str, letter: str) -> str:
    """Matches if firct character of word is letter"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


less_than_10(num=5)
