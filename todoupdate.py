import pickle
import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List')
        self.todo_list = []

        try:
            with open('todo_list.pkl', 'rb') as file:
                self.todo_list = pickle.load(file)
        except FileNotFoundError:
            pass

        self.task_entry = tk.Entry(root, font=('Arial', 18))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.grid(row=0, column=2, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, font=('Arial', 14), selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.load_tasks()

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.append(task)
            self.task_entry.delete(0, tk.END)
            self.load_tasks()
            self.save_tasks()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            new_task = self.task_entry.get()
            if new_task:
                self.todo_list[selected_index] = new_task
                self.load_tasks()
                self.save_tasks()
        else:
            messagebox.showerror("Error", "Please select a task to update.")

    def save_tasks(self):
        with open('todo_list.pkl', 'wb') as file:
            pickle.dump(self.todo_list, file)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

