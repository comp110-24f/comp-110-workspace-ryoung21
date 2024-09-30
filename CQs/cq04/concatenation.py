"""Concatenation"""

__author__ = "730461441"


def concat(string1: str, string2: str) -> str:
    """return the concatenation of string1 and string2"""
    return string1 + string2


word1: str = "happy"
word2: str = "tuesday"
if __name__ == "__main__":
    print(concat(word1, word2))
