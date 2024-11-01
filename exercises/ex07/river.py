"""File to define River class."""

from ex07.fish import Fish
from ex07.bear import Bear


class River:
    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Removes old bears and fish from fish/bears list."""
        # Initiate empty lists to put surviving animals
        surviving_bears: list[Bear] = []
        surviving_fish: list[Fish] = []

        # Adds young animals to surviving lists
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)

        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)

        # Make sure to set arrtibutes equal to list
        self.fish = surviving_fish
        self.bears = surviving_bears
        return None

    def remove_fish(self, amount: int) -> None:
        """Removes frontmost objects part of self.fish list by amount."""
        kept_fish: list[Fish] = []

        # Access objects at specified indexes
        for index in range(amount, len(self.fish)):
            kept_fish.append(self.fish[index])

        # Update self.attribute
        self.fish = kept_fish
        return None

    def bears_eating(self) -> None:
        """Bears eat fish using eat() and remove_fish()"""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self) -> None:
        """Removes bears with low hunger score."""
        surviving_bears: list[Bear] = []

        # Distinguishes which bears have survived
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)

        self.bears = surviving_bears
        return None

    def repopulate_fish(self) -> None:
        """Adds newborn fish objects to fish attribute."""
        new_fish_count: int = (len(self.fish) // 2) * 4

        # Adds object for each born fish into self.fish list
        for _ in range(0, new_fish_count):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self) -> None:
        """Adds newborn bear objects to bears attribute."""
        # Determines of bears born
        new_bear_count: int = len(self.bears) // 2

        for _ in range(0, new_bear_count):
            self.bears.append(Bear())
        return None

    def view_river(self) -> None:
        print(f"~~~ Day {self.day}: ~~~")
        # length of lists gets total count
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Calls one_river_day seven times."""
        for _ in range(0, 7):
            self.one_river_day()
            print(self.bears[0].hunger_score)
