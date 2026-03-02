# Method 1:
# def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
#     name = seed_type.capitalize()
#     if unit == "packets":
#         output = f"{name} seeds: {quantity} {unit} available"
#     elif unit == "grams":
#         output = f"{name} seeds: {quantity} {unit} total"
#     elif unit == "area":
#         output = f"{name} seeds: covers {quantity} square meters"
#     else:
#         output = "Unknown unit type."
#     print(output)

# Method 2:
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    name = seed_type.capitalize()
    match unit:
        case "packets":
            print(f"{name} seeds: {quantity} {unit} available")
        case "grams":
            print(f"{name} seeds: {quantity} {unit} total")
        case "area":
            print(f"{name} seeds: covers {quantity} square meters")
        case _:
            print("Unknown unit type.")
