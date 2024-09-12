"""Get weather report function"""


def get_weather_report() -> str:
    """describes weather and what you should do"""
    weather: str = input("What is the weather? ")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
