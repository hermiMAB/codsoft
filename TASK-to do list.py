import tkinter as tk
from tkinter import ttk

def add_task():
    task_description = task_entry.get()
    # Update the task listbox
    task_listbox.insert(tk.END, task_description)
    # Clear the entry field
    task_entry.delete(0, tk.END)
window = tk.Tk()
window.title("To-Do List")

# Task Entry
task_label = tk.Label(window, text="Enter Task:")
task_label.pack()
task_entry = tk.Entry(window)
task_entry.pack()

# Add Task Button
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()

# Task Listbox
task_listbox = tk.Listbox(window)
task_listbox.pack()

window.mainloop()