

with open("log1.txt", "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Python is present. line no : {lineno}")
        break
    lineno +=1

else:
    print("Python is not present in the log file")