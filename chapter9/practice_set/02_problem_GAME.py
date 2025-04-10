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
'''
imported random to create a random score

created a function named game()
    printed a message
    made a variable to store random number as score gave it boundations as from 1 to 60
    using 'with' we opened the text file where score was being stored, read it as 'f'
    made a variable to read the file/function 
    if condition was applied, agar highscore blank nahi hai then read that as high score
    else condition was applied, agar highscore initially kuchh nhi hai then highScore = 0
    came out of if else
    in with, we printed the randomly generated {score}
    again if condition was applied: if the new generated score is high than already existing high score then:
                                                                            'with' that highScore.txt write as string the new generated score
        else print already jo score hai vo high hai
    then using return, we took/ pulled out the value of score
game() ended the function
'''