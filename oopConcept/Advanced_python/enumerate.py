l = [3, 513, 53, 535]

# index = 0

# for items in l:
#     print(f"The item number at index {index} is {items}")
#     index += 1

# This can be simplified by using the enumerate function

for index, items in enumerate(l):
    print(f"The item number at index {index} is {items}")