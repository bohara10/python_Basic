word = "donkey"

with open("message.txt", "r") as f:
    content = f.read()

contentNew = content.replace("donkey", "######")

with open("message.txt", "w") as f:
    f.write(contentNew)
