""" 
This task aims to design a password generator which ask user for
the length of the desired password and generates one
"""
import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password_gui():
    window = tk.Tk()
    window.title("Password Generator")
    window.geometry("400x200") 
    window.resizable(False, False) 

    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    window.grid_rowconfigure(3, weight=1)

    length_label = tk.Label(window, text="Enter Password Length:")
    length_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    length_entry = tk.Entry(window, width=10)
    length_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    length_entry.insert(0, "12")

    password_display_label = tk.Label(window, text="Generated Password:", wraplength=300)
    password_display_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    generated_password_entry = tk.Entry(window, width=40, state='readonly', justify='center')
    generated_password_entry.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def generate():
        try:
            length = int(length_entry.get())
            if length <= 0:
                messagebox.showerror("Invalid Input", "Password length must be a positive number.")
                return
            elif length > 100: 
                messagebox.showwarning("Length Warning", "Password length is very long. Consider a shorter length for usability.")
        
            characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))

            generated_password_entry.config(state='normal')
            generated_password_entry.delete(0, tk.END)
            generated_password_entry.insert(0, password) 
            generated_password_entry.config(state='readonly')

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid whole number for the password length.")

    generate_button = tk.Button(window, text="Generate Password", command=generate)
    generate_button.grid(row=1, column=0, columnspan=2, pady=10)

    window.mainloop()
generate_password_gui()
