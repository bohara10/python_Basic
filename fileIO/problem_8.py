with open("file.txt", "r") as f:
    content = f.read()

with open("file3.txt", "r") as f:
    content1 = f.read()

if(content == content1):
    print("Both files have same content and identical")

else:
    print("Both files have different content and not identical")