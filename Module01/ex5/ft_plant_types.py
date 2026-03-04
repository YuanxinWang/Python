#!/usr/bin/env python3

class Plant:
    # first set to zero to secure the data initialization in case of error
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Error: Invalid height {height}cm [REJECTED]")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Error: Invalid height {age} days [REJECTED]")
        else:
            self._age = age

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> str:
        return (f"{self._name}: {self._height}cm, {self._age} days")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color

    def bloom(self) -> None:
        print(f"{self._name} is blooming beautifully!")

    def get_info(self) -> str:
        return (
            f"{self._name} (Flower): {self._height}cm, "
            f"{self._age} days, {self._color} color"
        )


class Tree(Plant):
    def __init__(self, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"{self._name} provides "
            f"{self._trunk_diameter * 2} square meters of shade"
        )

    def get_info(self) -> str:
        return (
            f"{self._name} (Tree): {self._height}cm, "
            f"{self._age} days, {self._trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def nutrition(self) -> None:
        print(f"{self._name} is rich in {self._nutritional_value}")

    def get_info(self) -> str:
        return (
            f"{self._name} (Vegetable): {self._height}cm, "
            f"{self._age} days, {self._harvest_season}"
        )


def main() -> None:
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C")
    print("=== Garden Plant Types ===\n")
    print(rose.get_info())
    rose.bloom()
    print("")
    print(oak.get_info())
    oak.produce_shade()
    print("")
    print(tomato.get_info())
    tomato.nutrition()


if __name__ == "__main__":
    main()
