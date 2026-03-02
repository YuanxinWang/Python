# Method 1:
def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    if days < 1:
        print("Invalid input.")
    else:
        for i in range(1, days + 1):
            print("Day", i)
        print("Harvest time!")

# Method 2:
# def ft_count_harvest_iterative():
#     days = int(input("Days until harvest: "))
#     if days < 1:
#         print("Invalid input.")
#     else:
#         i = 1
#         while i <= days:
#             print("Day", i)
#             i += 1
#         print("Harvest time!")
