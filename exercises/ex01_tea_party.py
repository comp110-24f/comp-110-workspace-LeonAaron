"""This program will help to plan a tea party"""

__author__: str = "730741513"


def main_planner(guests: int) -> None:
    """Puts all functions together."""

    # Print information of screen and run functions
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """How many total tea bags does the party need?"""
    return people * 2


def treats(people: int) -> int:
    """Returns the number of treats needed for the party based on the number of peopole attending."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Returns the total cost of tea bags and treats for the party combined."""
    # Returns the total cost
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
