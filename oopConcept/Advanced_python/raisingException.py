a = int(input("Enter a number:   "))
b = int(input("Enter a number:   "))
 

if( b== 0 ):
    raise ZeroDivisionError("Cannot divide by zero")

print(f"The division of {a} and {b } is {a/b}")
