# greates among three numbers

# def greatest_of_three(a, b, c):
#     if(a > b and a > c):
#         return f"{a} is greatest number"
    
#     elif(b > a and b > c):
#         return f"{b} is greatest number"
#     else:
#         return f"{c} is greatest number"
    
# a = int(input("Enter a first number:"))
# b = int(input("Enter a second number:"))
# c = int(input("Enter a third number:"))

# print(greatest_of_three(a, b, c))

#  celcius to fahrenheit

def convert(c):
    # c = int(input("Enter a temperature in celcius: "))
    f = (c * 9/5) + 32

    return f

c = int(input("Enter a temperature in celcius: "))
print(convert(c))


