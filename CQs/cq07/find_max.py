"""cq07 - find_and_remove_max function"""

__author__ = "730461441"


def find_and_remove_max(ints: list[int]) -> int:
    if ints == []:  # return -1 if list is empty
        return -1

    max_value: int = ints[0]
    for num in ints:
        if num > max_value:
            max_value = num

    index: int = 0

    while index < len(ints):
        if ints[index] == max_value:
            ints.pop(index)
        index += 1

    return max_value
