#!/usr/bin/env python3

class Garden:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name: str = name
        self._height: int = height
        self._age: int = age

    def get_info(self) -> str:
        return f"Created: {self._name} ({self._height}cm, {self._age} days)"


def main() -> None:
    data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    garden = [
        Garden(plant[0], plant[1], plant[2])
        for plant in data
    ]
    print("=== Plant Factory Output ===")
    count = 0
    for plant in garden:
        print(plant.get_info())
        count += 1
    print(f"\nTotal plants created: {count}")


if __name__ == "__main__":
    main()
