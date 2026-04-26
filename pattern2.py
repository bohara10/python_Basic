'''
*
**
***

'''

# n = int(input("Enter the number of rows for the pattern: "))

# for i in range(1, n + 1):
#     print("*" * i, end="")

#     print("")


'''
* * *

* *   for n = 3

* * *

'''

n = int(input("Enter the number of rows for the pattern: "))

for i in range(1, n+1):
    if(i == 1 or i == n):
        print("*"*n , end="" )

    else:
        print("*" , end="" )

        print(" " * (n-2), end="" )

        print("*" , end="" )

    print("")