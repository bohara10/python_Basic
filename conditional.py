
# a = int(input("Enter a first number:"))

# b = int(input("Enter a second number:"))

# c = int(input("Enter a third number:"))

# if(a > b and a > c):
#     print(f"{a} is greatest number")

# elif(b > a and b > c):
#     print(f"{b} is greatest number")

# else:
#     print(f"{c} is greatest number")
    

a = int(input("Enter your age: "))

if(a % 2 == 0):
    print("Your age is even!")
    

if(a >= 18):
    print("Your eligible for voting")
    print("Congrats you successfully registered for voting")

elif(a < 18):
    print("your are not eligible for voting")

else:
    print("Your are under age for voting")

print("Thank you for using our voting registration system")