# Method 1:
def count_days(days, i):
    if i > days:
        print("Harvest time!")
    else:
        print("Day", i)
        count_days(days, i + 1)

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    if days < 1:
        print("Invalid input.")
    else:
        i = 1
        count_days(days, i)

# Method 2:
# def ft_count_harvest_recursive(i = 1, days2 = None):
#     if days2 is None:
#         days2 = int(input("Days until harvest: "))
#         if days2 < 1:
#             print("Invalid input.")
#             return
#     if i > days2:
#         print("Harvest time!")
#         return
#     print("Day", i)
#     ft_count_harvest_recursive(i + 1, days2)
