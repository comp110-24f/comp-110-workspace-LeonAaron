"""Challenge question- first function"""

__author__ = "730741513"


def mimic(message: str) -> str:
    """Takes input and repeats it back"""
    return message


def main() -> None:
    """Prints the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
