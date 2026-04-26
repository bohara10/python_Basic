import random


def game():
    print("Your are playing the game...")
    score = random.randint(1, 100)
    # Fetch the hiscore
    with open("score.txt") as f:
        hiScore = f.read()
    if (hiScore != ""):
        hiScore = int(hiScore)

    else:
        hiScore = 0

    print(f"your score: {score}")
    if score > hiScore or hiScore == "":
        # write this hiscore to the file
        with open("score.txt", "w") as f:
            f.write(str(score))

    return score


game()