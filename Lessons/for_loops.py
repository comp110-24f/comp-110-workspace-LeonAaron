"""For Loop syntax in python."""

pets: list[str] = ["Louie", "Bo", "Bear"]

for item in pets:
    print(f"Good boy, {item}!")


# Using the range function to get items and indecies
names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for index in range(0, len(names)):
    print(f"{index}: {names[index]}")
