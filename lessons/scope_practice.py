"""Some scope examples"""


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed"""
    copy: str = ""  # set up an empty string and then we can copy values over
    index: int = 0
    # print(word)  # can still access word because global variable
    while index < len(msg):
        if char != msg[index]:
            copy = copy + msg[index]
        index += 1
    return copy


# remove_chars("football", "o") -> "ftball"

if (
    __name__ == "__main__"
):  # so that lines of code will not be run if importing aspects to another file
    word: str = "yoyo"  # global variable
    print(remove_chars(word, "y"))
    print(remove_chars(word, "o"))
