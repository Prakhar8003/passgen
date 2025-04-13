import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyperclip
from password_generator import generate_password

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Title
        title_label = ttk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Length
        ttk.Label(root, text="Password Length:").pack()
        self.length_var = tk.IntVar(value=12)
        ttk.Spinbox(root, from_=4, to=64, textvariable=self.length_var, width=10).pack(pady=5)

        # Character options
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)

        ttk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=self.uppercase_var).pack(anchor="w", padx=20)
        ttk.Checkbutton(root, text="Include Lowercase (a-z)", variable=self.lowercase_var).pack(anchor="w", padx=20)
        ttk.Checkbutton(root, text="Include Digits (0-9)", variable=self.digits_var).pack(anchor="w", padx=20)
        ttk.Checkbutton(root, text="Include Symbols (!@#...)", variable=self.symbols_var).pack(anchor="w", padx=20)

        # Generate Button
        ttk.Button(root, text="Generate Password", command=self.generate_password).pack(pady=10)

        # Output field
        self.result_var = tk.StringVar()
        ttk.Entry(root, textvariable=self.result_var, width=35, font=("Courier", 12)).pack(pady=5)

        # Copy Button
        ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(pady=5)

    def generate_password(self):
        try:
            password = generate_password(
                length=self.length_var.get(),
                use_upper=self.uppercase_var.get(),
                use_lower=self.lowercase_var.get(),
                use_digits=self.digits_var.get(),
                use_symbols=self.symbols_var.get()
            )
            self.result_var.set(password)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def copy_to_clipboard(self):
        pyperclip.copy(self.result_var.get())
        messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

