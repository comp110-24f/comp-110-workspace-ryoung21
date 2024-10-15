"""EX05 - 'list' Utility Functions"""

__author__ = "730461441"


def only_evens(ints: list[int]) -> list[int]:
    index: int = 0
    new_ints: list[int] = []
    while index < len(ints):
        if ints[index] % 2 == 0:
            new_ints.append(ints[index])
        index += 1
    return new_ints


def sub(ints: list[int], start_index: int, end_index: int) -> list[int]:
    new_ints: list[int] = []
    if start_index < 0:
        start_index = 0
    if end_index > len(ints):
        end_index = len(ints)
    if len(ints) == 0:
        return new_ints
    if start_index >= len(ints):
        return new_ints
    if end_index <= 0:
        return new_ints
    for idx in range(start_index, end_index):
        new_ints.append(ints[idx])
    return new_ints


def add_at_index(ints: list[int], elem: int, index_added: int) -> None:
    if index_added < 0 or index_added > len(ints):
        raise IndexError("Index is out of bounds for the input list")
    ints.append(0)  # add space at end
    for idx in range(len(ints) - 1, index_added, -1):
        ints[idx] = ints[idx - 1]
    ints[index_added] = elem
