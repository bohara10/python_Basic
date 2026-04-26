'''
a = " a very long string with emails "

'''

## FIle read

# f = open("file.txt")

# data= f.read()

# print(data)

# f.close()
# lines= f.readlines()

f = open("file.txt")


# line1 = f.readline()

# print(line1, type(line1))

# line2= f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4 ="")

##
line= f.readline()

while(line !=""):
    print(line)
    line = f.readline()


f.close()

st = "Hey Rajan how ae you doing? "

f = open("myFile.txt", "a")

f.write(st)
f.close()


## file write 

# st = "this is new line"

# f= open("myFile.txt", "w")

# f.write(st)

# f.close()

