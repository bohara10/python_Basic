# f = open("file.txt")

# print(f.read())
# f.close()


#The same can be written using with statement like this

with open("file.txt") as f:
    print(f.read())

# you don't need to close the file when you are using with statement because it automatically closes the file after the block of code is executed.