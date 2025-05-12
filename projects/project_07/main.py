from english_words import get_english_words_set
from tkinter import *
import tkinter.font as font
import random

# Global variables to track game state
score = 0
missed = 0
time_elapsed = 0
count = 0
words = list(get_english_words_set(['web2']))

# Function to start the game
def startGame():
    welcome_window.destroy()
    game_window()

# Function to create and handle the game window
def game_window():
    global wn, nextWord, userInput, scoreboard, timer, scorelabel, timerlabel

    wn = Tk()
    wn.geometry('700x600')
    wn.title('Typing Test')
    wn.config(bg='honeydew2')

    Label(wn, text='Typing Test',
          font=('arial', 25, 'italic bold'),
          fg='gray', width=40).place(x=10, y=10)

    scorelabel = Label(wn, text='Your Score:',
                       font=('arial', 25, 'italic bold'), fg='red')
    scorelabel.place(x=10, y=100)

    scoreboard = Label(wn, text=score,
                       font=('arial', 25, 'italic bold'), fg='blue')
    scoreboard.place(x=100, y=180)

    timerlabel = Label(wn, text='Time Elapsed:',
                       font=('arial', 25, 'italic bold'), fg='red')
    timerlabel.place(x=500, y=100)

    timer = Label(wn, text=time_elapsed,
                  font=('arial', 25, 'italic bold'), fg='blue')
    timer.place(x=560, y=180)

    nextWord = Label(wn, text='Hit Enter to start and after typing the word',
                     font=('arial', 20, 'italic bold'), fg='black')
    nextWord.place(x=30, y=240)

    userInput = Entry(wn, font=('arial', 25, 'italic bold'),
                      bd=10, justify='center')
    userInput.place(x=150, y=330)
    userInput.focus_set()

    wn.bind('<Return>', mainGame)

    # Attach to global scope
    globals().update(locals())

    wn.mainloop()

# Function to update the timer and manage game ending
def timeFunc():
    global time_elapsed, score, missed, count

    if count <= 10:
        time_elapsed += 1
        timer.config(text=time_elapsed)
        timer.after(1000, timeFunc)
    else:
        showResults()

# Function to display final results and reset state
def showResults():
    global score, missed, time_elapsed, count, wn

    # Calculate WPM
    wpm = (score / time_elapsed) * 60 if time_elapsed > 0 else 0
    wpm = round(wpm, 2)

    result_text = (f'Time taken = {time_elapsed} sec\n'
                   f'Score = {score}\n'
                   f'Missed = {count-score-1}\n'
                   f'WPM = {wpm}')

    result_label = Label(wn, text=result_text, font=('arial', 22, 'italic bold'), fg='grey')
    result_label.place(x=150, y=230)

    # Restart Button
    restart_button = Button(wn, text="Restart", font=('arial', 18, 'bold'),
                            bg='light green', fg='black', command=restartGame)
    restart_button.place(x=300, y=450)

    # Destroy widgets
    for widget in (nextWord, userInput, scorelabel, scoreboard, timerlabel, timer):
        widget.destroy()

# Function handling main game logic
def mainGame(event):
    global score, missed, count, time_elapsed

    if time_elapsed == 0:
        random.shuffle(words)
        nextWord.config(text=words[0])
        userInput.delete(0, END)
        timeFunc()

    elif userInput.get() == nextWord['text']:
        score += 1
        scoreboard.config(text=score)

    count += 1
    if count <= 10:
        random.shuffle(words)
        nextWord.config(text=words[0])
        userInput.delete(0, END)

# Function to restart game
def restartGame():
    global score, missed, time_elapsed, count
    wn.destroy()  # Close current game window
    score = missed = time_elapsed = count = 0
    game_window()  # Start new game

# Welcome window setup
welcome_window = Tk()
welcome_window.geometry('600x600')
welcome_window.title("Typing Test")
welcome_window.config(bg='LightBlue1')

Frame(welcome_window, bg="snow3", bd=5).place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.16)

Label(welcome_window, text="Welcome to \n Typing Test",
      bg='azure2', fg='black', font=('Courier', 15, 'bold')).place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.16)

Button(welcome_window, text="Start", bg='old lace', fg='black',
       width=20, height=2, font=font.Font(size=12), command=startGame).place(x=200, y=300)

welcome_window.mainloop()
