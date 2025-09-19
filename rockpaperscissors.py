import tkinter as tk
import random

# Game logic
def get_computer_choice():
    return random.choice(['✊ Rock', '📄 Paper', '✂️ Scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "🤝 It's a Tie!"
    elif (user == '✊ Rock' and computer == '✂️ Scissors') or \
         (user == '✂️ Scissors' and computer == '📄 Paper') or \
         (user == '📄 Paper' and computer == '✊ Rock'):
        return "✅ You Win!"
    else:
        return "❌ You Lose!"

def play(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    result_label.config(text=f"🧑 You: {user_choice}\n💻 Computer: {computer_choice}", fg="#333")
    outcome_label.config(text=result, fg="#006400" if "Win" in result else "#8B0000" if "Lose" in result else "#444")

    if "Win" in result:
        scores['user'] += 1
    elif "Lose" in result:
        scores['computer'] += 1

    score_label.config(text=f"📊 Score — You: {scores['user']} | Computer: {scores['computer']}")
    play_again_button.config(state=tk.NORMAL)

def reset_game():
    result_label.config(text="")
    outcome_label.config(text="")
    play_again_button.config(state=tk.DISABLED)

# GUI setup
root = tk.Tk()
root.title("🎮 Rock-Paper-Scissors Game")
root.geometry("420x360")
root.configure(bg="#f0f8ff")
root.resizable(False, False)

scores = {'user': 0, 'computer': 0}

title_label = tk.Label(root, text="🎮 Rock-Paper-Scissors", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#1e90ff")
title_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack()

choices = ['✊ Rock', '📄 Paper', '✂️ Scissors']
colors = ['#ff6347', '#3cb371', '#1e90ff']

for i, choice in enumerate(choices):
    btn = tk.Button(button_frame, text=choice, width=12, font=("Helvetica", 12, "bold"),
                    bg=colors[i], fg="white", command=lambda c=choice: play(c))
    btn.pack(side=tk.LEFT, padx=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f8ff")
result_label.pack(pady=10)

outcome_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#f0f8ff")
outcome_label.pack(pady=5)

score_label = tk.Label(root, text="📊 Score — You: 0 | Computer: 0", font=("Helvetica", 12), bg="#f0f8ff", fg="#333")
score_label.pack(pady=10)

play_again_button = tk.Button(root, text="🔁 Play Again", font=("Helvetica", 12),
                              command=reset_game, state=tk.DISABLED, bg="#ffa500", fg="white")
play_again_button.pack(pady=5)

exit_button = tk.Button(root, text="❌ Exit", command=root.quit, font=("Helvetica", 12),
                        bg="#dc143c", fg="white")
exit_button.pack(pady=5)

root.mainloop()