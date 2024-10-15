"""ex04_utils"""

__author__ = "730461441"


def all(ints_list: list[int], given_int: int) -> bool:
    """Returns a bool indicating if the ints in ints_list are the same as given_int."""
    index: int = 0
    while index < len(ints_list):
        if given_int != ints_list[index]:
            return False
        index += 1
    return True


def max(input: list[int]) -> int:
    """Returns largest int in input."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_int: int = input[0]
    index: int = 1
    while index < len(input):
        if input[index] > max_int:
            max_int = input[index]
        index += 1
    return max_int


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns True if every element at every index of each list is equal."""
    if len(list1) != len(list2):
        return False
    index: int = 0
    while index < len(list1):
        if (
            list1[index] != list2[index]
        ):  # cannot use == and return True here, this order is crucial
            return False
        index += 1
    return True


def extend(intlist1: list[int], intlist2: list[int]) -> None:
    """Mutates intlist1 by appending the second lists's values to the end of it."""
    index: int = 0
    while index < len(intlist2):
        intlist1.append(intlist2[index])
        index += 1
