import tkinter as tk
import random

# Game options
choices = ["Rock", "Paper", "Scissors"]

# Scores
user_score = 0
computer_score = 0

# Function to play game
def play(choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    result = ""

    if choice == computer_choice:
        result = "It's a Tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    # Update labels
    user_label.config(text=f"You: {choice}")
    computer_label.config(text=f"Computer: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score → You: {user_score} | Computer: {computer_score}")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x300")

# Labels
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold")).pack(pady=10)
user_label = tk.Label(root, text="You: ", font=("Arial", 12))
user_label.pack()
computer_label = tk.Label(root, text="Computer: ", font=("Arial", 12))
computer_label.pack()
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=10)
score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack()

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

for choice in choices:
    tk.Button(button_frame, text=choice, width=10, height=2,
              command=lambda ch=choice: play(ch)).pack(side="left", padx=10)

# Run the application
root.mainloop()
