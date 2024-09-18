def characters(msg: str) -> None:
    index: int = 0
    while index < len(msg):
        print(msg[index])
        index = index + 1  # can also do index += 1


characters(msg="Howdy")
# print("Howdy".lower()) for lower case
