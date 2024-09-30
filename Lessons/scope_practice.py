"""Practice scope"""


def remove_chars(msg: str, char: str) -> str:
    """Return copy of meg with all chars removed"""

    copy: str = ""
    index: int = 0

    while index < len(msg):
        if not (msg[index] == char):
            copy += msg[index]
        index += 1
    return copy


word: str = "yoyo"  # global variable

if __name__ == "__main__":

    print(remove_chars(msg=word, char="y"))
