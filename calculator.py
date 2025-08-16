import tkinter as tk
from tkinter import messagebox
import os

# Functions
def press_number(num):
    entry_num1.insert(tk.END, str(num))

def press_operator(op):
    global operator, first_number
    operator = op
    try:
        first_number = float(entry_num1.get())
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")
        return
    entry_num1.delete(0, tk.END)

def calculate():
    try:
        num2 = float(entry_num1.get())
        result = None
        if operator == "+":
            result = first_number + num2
        elif operator == "-":
            result = first_number - num2
        elif operator == "*":
            result = first_number * num2
        elif operator == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = first_number / num2
        else:
            messagebox.showerror("Error", "Invalid operator")
            return
        entry_num1.delete(0, tk.END)
        entry_num1.insert(0, str(result))
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")

def clear():
    entry_num1.delete(0, tk.END)

# Window setup
root = tk.Tk()
root.title("Pixel Calculator")
root.geometry("500x600")
root.resizable(False, False)

# Set icon
icon_path = os.path.join(os.path.dirname(__file__), "pixel_icon.ico")
try:
    root.iconbitmap(icon_path)
except Exception:
    pass

# Font
font_style = ('Fredoka One', 20, 'bold')  # Make sure Fredoka One is installed

# Entry
entry_num1 = tk.Entry(root, width=16, font=font_style, borderwidth=2, relief='ridge', justify='left')
entry_num1.grid(row=0, column=0, columnspan=4, pady=20, padx=10, ipadx=10)


# Button layout and colors
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

operator = ''
first_number = 0

for (text, row, col) in buttons:
    if text in '+-*/=':
        bg_color = '#FF9500'  # Orange for operators
        fg_color = 'white'
        action = calculate if text == '=' else lambda x=text: press_operator(x)
    else:
        bg_color = '#87CEEB'  # Sky blue for numbers
        fg_color = 'black'
        action = lambda x=text: press_number(x)

    btn = tk.Button(root, text=text, width=5, height=2, font=font_style,
                    bg=bg_color, fg=fg_color, activebackground='#00CED1', activeforeground='white',
                    command=action)
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(root, text='C', width=5, height=2, font=font_style,
          bg='#FF3B30', fg='white', activebackground='#FF6347', command=clear)\
    .grid(row=5, column=0, columnspan=4, sticky='we', padx=5, pady=5)

root.mainloop()
