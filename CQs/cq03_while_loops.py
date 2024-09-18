"""CQ03"""

__author__ = "730461441"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(phrase):  # keeps from looping indefinitely
        if (
            search_char == phrase[index]
        ):  # if the character matches index of phrase, count increases
            count = count + 1
        index = index + 1
    return count
