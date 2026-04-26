# # a = 12
# # b = 45
# # c = 56

# # avg = (a + b + c) / 3

# # print(avg)

# # a = 3
# # b = 2
# # c = 1

# # avg = (a + b + c) / 3


# def avg():
#     a = int(input("Enter a first number:"))
#     b = int(input("Enter a second number:"))
#     c = int(input("Enter a third number:"))

#     average = (a + b + c) / 3

    

#     print(f"The average of {a}, {b} and {c} is {average}")

# # for i in range(2):
# #     i += 1
# #     avg()




# ##

# def greet():

#     print("Good Day!")


# greet()

# function with arguments

# def greet(name, ending):
#     print("Good Day!" + name)
#     print(ending)

#     return "Ok"

# a = greet(" Rajan ", "Have a nice day!")
# # greet(" Rohan ", "Thank you for using our services!")

# print(a)

# Default arguments

def greet(name = "Rajan", ending = "Thank You!"):
    print("Good Day!" + name)
    print(ending)


greet("Harry")
greet()

