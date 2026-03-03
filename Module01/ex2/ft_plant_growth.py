#!/usr/bin/env python3

class Garden:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name: str = name
        self._height: int = height
        self._age: int = age

    def grow(self, num: int) -> None:
        self._height += num

    def age(self, days: int) -> None:
        self._age += days

    def get_info(self) -> str:
        return f"{self._name}: {self._height}cm, {self._age} days old"


def main() -> None:
    rose = Garden("Rose", 25, 30)
    initial = rose._height
    print("=== Day 1 ===")
    print(rose.get_info())
    for _ in range(6):
        rose.grow(1)
        rose.age(1)
    print("=== Day 7 ===")
    print(rose.get_info())
    growth = rose._height - initial
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    main()
