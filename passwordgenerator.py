import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Invalid Length", "Password length should be at least 4.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

root = tk.Tk()
root.title("Secure Credential Generator")
root.geometry("420x320")
root.configure(bg="#79d3f7")
root.resizable(False, False)

label_font = ("Helvetica", 12, "bold")
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")
button_bg = "#4CAF50"
button_fg = "white"

tk.Label(root, text="Enter Username:", font=label_font, bg="#79d3f7").pack(pady=(15, 5))
username_entry = tk.Entry(root, font=entry_font, justify='center', width=30)
username_entry.pack()

tk.Label(root, text="Enter Password Length:", font=label_font, bg="#79d3f7").pack(pady=(15, 5))
length_entry = tk.Entry(root, font=entry_font, justify='center', width=30)
length_entry.pack()

tk.Button(root, text="Generate Password", font=button_font, bg=button_bg, fg=button_fg,
          activebackground="#45a049", command=generate_password).pack(pady=15)

tk.Label(root, text="Generated Password:", font=label_font, bg="#79d3f7").pack()
password_entry = tk.Entry(root, font=entry_font, justify='center', width=30)
password_entry.pack()

tk.Label(root, text="Designed by Payal 💡", font=("Helvetica", 10), bg="#79d3f7", fg="#888").pack(pady=10)

root.mainloop()