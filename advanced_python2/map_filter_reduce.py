# Map Example
from functools import reduce
l = [1, 2, 3, 4, 5]

square = lambda x: x * x
sqlist = map(square, l)

print(list(sqlist))

#Filter Example

def even(n):
    if (n%2== 0):
        return True
    return False
onlEven = filter(even, l)

print(list(onlEven) )



# Reduce Example

def sum(a, b):
    return a + b

mul = lambda a, b: a * b

print(reduce(sum , l))

print(reduce(mul, l))