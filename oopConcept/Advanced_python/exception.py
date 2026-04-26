try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError as v:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    print(e)


print("Thank You")