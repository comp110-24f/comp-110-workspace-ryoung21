"""Mutating functions."""

__author__ = "730461441"


def manual_append(a: list, i: int) -> None:
    """mutates its input by appending i parameter to the end of a[i] parameter"""
    a.append(a[i])


def double(d: list) -> None:
    """mutates its input by multiplying every element in the d[index] parameter by 2"""
    index: int = 0
    while index < len(d):
        d[index] = d[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
