import tkinter as tk


window = tk.Tk()
window.title("Calculator")
window.geometry("350x500")

frame = tk.Frame(window, bg="white", padx=100,pady=100)
frame.pack(padx=20, pady=20)

label = tk.Label(window, text = "CALCULATOR",font=("Arial",20,"bold"))
label.pack(pady=(5,0))

entry = tk.Entry(window, font=("Arial", 20), bd=10, relief="sunken", justify="right")
entry.pack(fill="both", padx=10, pady=10)

# Function to handle button press
def press(char):
    if char == "C":
        entry.delete(0, tk.END)
    elif char == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, char)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

# Frame for buttons
btn_frame = tk.Frame(window)
btn_frame.pack()

# Create buttons in grid
for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        btn = tk.Button(btn_frame, text=char, width=5, height=2, font=("Arial", 16),
                        command=lambda ch=char: press(ch))
        btn.grid(row=r, column=c, padx=5, pady=5)

# Run the app
window.mainloop()
