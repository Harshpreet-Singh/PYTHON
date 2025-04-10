import random

def game():
    print("You are playing the Game...")
    score = random.randint(1, 61)
    with open("highScore.txt") as f:
        highScore = f.read()
        if(highScore !=""):
            highScore = int(highScore)
        else:
            highScore = 0
    print(f"Your score: {score}")
    if(score>int(highScore)):
        with open("highScore.txt") as f:
        highScore = f.read()
        # then write the new score as high score
    return score