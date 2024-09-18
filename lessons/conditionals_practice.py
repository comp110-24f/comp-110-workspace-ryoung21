def wake_up(alarm: bool) -> str:
    """Return a message based on if alarm is going off."""
    if alarm is True:
        return "Wake up! Go to Comp110!"
    else:
        return "Keep sleeping. You deserve is. :)"


def check_first_letter(word: str, letter: str) -> str:
    """Returns match! if the first character of word is letter"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


def get_weather_report() -> str:
    """asks user what is weather and returns suggestion"""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
