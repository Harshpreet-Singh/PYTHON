import random

def game():
    print("\nYou are playing the Game...\n")
    score = random.randint(1, 61)
    with open("chapter9\practice_set\highScore.txt") as f:
        highScore = f.read()
        if(highScore !=""):
            highScore = int(highScore)
        else:
            highScore = 0

    print(f"Your score: {score}")
    if(score>highScore):
        with open("chapter9\practice_set\highScore.txt", "w") as f:
            f.write(str(score))
        # then write the new score as high score
    else:
        print(f"\nThis is not a High Score\nScore Greater than this already exists i.e. {highScore}")
    return score

game()