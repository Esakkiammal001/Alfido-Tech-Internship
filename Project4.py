import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

root = tk.Tk()
root.title("Simple To-Do List")
root.geometry("400x400")
root.resizable(False, False)

tk.Label(root, text="Enter a task:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack()

tk.Button(root, text="Add Task", command=add_task, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Remove Selected Task", command=remove_task, font=("Arial", 12)).pack(pady=5)

listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=15)
listbox.pack(pady=10)

root.mainloop()
