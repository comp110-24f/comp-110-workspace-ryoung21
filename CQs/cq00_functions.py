"""CQ00"""

__author__ = "730461441"


def mimic(message: str) -> str:
    "Returns message"
    return message


def main() -> None:
    "Prints result of calling mimic"
    return print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
