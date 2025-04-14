import winsound
import tkinter as tk
from random import randint

# Global state
n = randint(1, 100)
guesses = [0]
def type_intro_text(text, index=0):
    if index < len(text):
        intro_label.config(text=text[:index+1])
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS | winsound.SND_ASYNC)
        root.after(60, type_intro_text, text, index + 1)
    else:
        winsound.PlaySound(None, winsound.SND_PURGE)
        root.after(800, show_game_ui)
winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)


# Main window setup
root = tk.Tk()
root.title("🎮 Number Guessing Game")
root.geometry("420x400")
root.configure(bg="#f0f4f8")

# --- INTRO ANIMATION ---
intro_frame = tk.Frame(root, bg="#f0f4f8")
intro_frame.pack(fill="both", expand=True)

intro_label = tk.Label(
    intro_frame,
    text="",
    font=("Helvetica", 20, "bold"),
    bg="#f0f4f8",
    fg="#2c3e50"
)
intro_label.pack(pady=150)

def type_intro_text(text, index=0):
    if index < len(text):
        intro_label.config(text=text[:index+1])
        root.after(60, type_intro_text, text, index + 1)
    else:
        root.after(800, show_game_ui)

# --- MAIN GAME UI ---
game_frame = tk.Frame(root, bg="#f0f4f8")

def reset_game():
    global n
    n = randint(1, 100)
    guesses[0] = 0
    result_label.config(text="", fg="#333")
    entry.delete(0, tk.END)
    submit_button.config(state="normal")
    replay_button.pack_forget()

def check_guess():
    try:
        a = int(entry.get())
        guesses[0] += 1

        if a == n:
            result_label.config(
                text=f"🎉 You won!\nThe number was {n}.\nTotal guesses: {guesses[0]}",
                fg="#27ae60"
            )
            submit_button.config(state="disabled")
            replay_button.pack(pady=10)
        elif a < 0:
            result_label.config(text="The number is positive!", fg="#c0392b")
        elif a > n:
            result_label.config(text=f"📉 Guess a lower number than {a}", fg="#2980b9")
        elif a < n:
            result_label.config(text=f"📈 Guess a greater number than {a}", fg="#8e44ad")
        else:
            result_label.config(text="Oops, something went wrong!", fg="#e74c3c")
    except ValueError:
        result_label.config(text="❌ Please enter a valid number!", fg="#e74c3c")

def show_game_ui():
    intro_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)

    tk.Label(
        game_frame, 
        text="Guess the Number (1-100)", 
        font=("Helvetica", 18, "bold"), 
        bg="#f0f4f8", 
        fg="#2c3e50"
    ).pack(pady=20)

    global entry, submit_button, result_label, replay_button

    entry = tk.Entry(
        game_frame, font=("Helvetica", 16),
        width=15, justify="center", relief="groove", bd=3
    )
    entry.pack(pady=10)

    submit_button = tk.Button(
        game_frame, text="🎯 Submit Guess", font=("Helvetica", 14, "bold"),
        bg="#3498db", fg="white", activebackground="#2980b9",
        relief="flat", padx=10, pady=5, command=check_guess
    )
    submit_button.pack(pady=10)

    result_label = tk.Label(
        game_frame, text="", font=("Helvetica", 13),
        bg="#f0f4f8", wraplength=350, justify="center"
    )
    result_label.pack(pady=10)

    replay_button = tk.Button(
        game_frame, text="🔁 Play Again", font=("Helvetica", 14, "bold"),
        bg="#2ecc71", fg="white", activebackground="#27ae60",
        relief="flat", padx=10, pady=5, command=reset_game
    )

# Start the intro animation
type_intro_text("🎮 Welcome to the Number Guessing Game!")

# Run the app
root.mainloop()
