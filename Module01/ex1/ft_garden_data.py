#!/usr/bin/env python3

class Garden:
	def __init__(self, name: str, height: int, age: int) -> None:
		self.name: str = name
		self.height: int = height
		self.age: int = age

def main() -> None:
	rose = Garden("Rose", 25, 30)
	sunflower = Garden("Sunflower", 80, 45)
	cactus = Garden("Cuctus", 15,120)
	garden: list[Garden] = [rose, sunflower, cactus]
	print("=== Garden Plant Registry ===")
	for plant in garden:
		print(f"{plant.name}: {plant.height}cm, {plant.age} days old")

if __name__ == "__main__":
	main()