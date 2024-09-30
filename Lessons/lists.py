"""Creates an empty list of floats"""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructoin


# String analogy
# my_name: str = "" #literal
# my_name: str = str()

# Adding a value to a list
my_numbers.append(1.5)
my_numbers.append(2.3)

# Populated list
game_points: list[int] = [102, 86, 94]

# Modifies index
game_points[1] = 72

print(my_numbers)
print(game_points)

# Indexes list
last_game: int = game_points[2]

print(last_game)


# class_num: str = "110"  # Change to "210"

# Creates error
# class_num[0]  = "2"


# Gets length of list
game_points_length: int = len(game_points)
print(game_points_length)


# removes item from list
game_points.pop(1)
print(game_points)


def display(int_list: list[int]) -> None:

    index: int = 0

    while index < len(int_list):
        print(int_list[index])
        index += 1


display(int_list=game_points)
