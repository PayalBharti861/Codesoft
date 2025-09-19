import tkinter as tk
from tkinter import messagebox

pending_tasks = []
completed_tasks = []

def add_task():
    task = task_entry.get()
    if task:
        pending_tasks.append(task)
        update_listboxes()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def add_preloaded_task(task):
    pending_tasks.append(task)
    update_listboxes()

def mark_completed():
    selected = pending_listbox.curselection()
    if selected:
        task = pending_tasks.pop(selected[0])
        completed_tasks.append(task)
        update_listboxes()
    else:
        messagebox.showwarning("Selection Error", "Select a pending task to mark as completed.")

def delete_completed():
    selected = completed_listbox.curselection()
    if selected:
        completed_tasks.pop(selected[0])
        update_listboxes()
    else:
        messagebox.showwarning("Selection Error", "Select a completed task to delete.")

def update_listboxes():
    pending_listbox.delete(0, tk.END)
    for task in pending_tasks:
        pending_listbox.insert(tk.END, f"❌ {task}")
    
    completed_listbox.delete(0, tk.END)
    for task in completed_tasks:
        completed_listbox.insert(tk.END, f"✅ {task}")

# GUI setup
root = tk.Tk()
root.title("Payal's To-Do List")
root.geometry("500x750")
root.configure(bg="#eafc4a")
root.resizable(False, False)

# Fonts and colors
label_font = ("Helvetica", 16, "bold")
entry_font = ("Helvetica", 14)
button_font = ("Helvetica", 13, "bold")
button_bg = "#4CAF50"
button_fg = "white"

# Task input
tk.Label(root, text="Enter a Task:", font=label_font, bg="#eafc4a").pack(pady=10)
task_entry = tk.Entry(root, font=entry_font, width=30, justify='center')
task_entry.pack()

tk.Button(root, text="Add Task", font=button_font, bg=button_bg, fg=button_fg,
          activebackground="#45a049", command=add_task).pack(pady=10)

# Preloaded task options
tk.Label(root, text="Quick Add Tasks:", font=label_font, bg="#eafc4a").pack(pady=10)
preloaded_frame = tk.Frame(root, bg="#f0f4f7")
preloaded_frame.pack()

preloaded_tasks = ["Wake Up", "Bath", "Study"]
for task in preloaded_tasks:
    tk.Button(preloaded_frame, text=task, font=("Helvetica", 12), bg="#e0e0e0", fg="black",
              width=25, command=lambda t=task: add_preloaded_task(t)).pack(pady=3)

# Pending tasks
tk.Label(root, text="Pending Tasks:", font=label_font, bg="#eafc4a").pack(pady=10)
pending_listbox = tk.Listbox(root, font=entry_font, width=40, height=5, selectbackground="#ffe0e0")
pending_listbox.pack()

tk.Button(root, text="Mark as Completed", font=button_font, bg="#2196F3", fg="white",
          activebackground="#1976D2", command=mark_completed).pack(pady=5)

# Completed tasks
tk.Label(root, text="Completed Tasks:", font=label_font, bg="#eafc4a").pack(pady=10)
completed_listbox = tk.Listbox(root, font=entry_font, width=40, height=5, selectbackground="#e0ffe0")
completed_listbox.pack()

tk.Button(root, text="Delete Completed Task", font=button_font, bg="#f44336", fg="white",
          activebackground="#d32f2f", command=delete_completed).pack(pady=5)

# Footer
tk.Label(root, text="Designed by Payal 💼", font=("Helvetica", 12), bg="#eafc4a", fg="#888").pack(pady=6)

# Run the app
root.mainloop()