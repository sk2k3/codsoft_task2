import tkinter as tk
from tkinter import StringVar

class Calculator:
    def __init__(self, root):
        root.title("Simple Calculator")
        root.geometry('400x500')
        root.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''

        # Entry widget for displaying the equation
        entry = tk.Entry(root, textvariable=self.equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        # Define buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]

        # Create buttons and assign them to a grid
        for (text, row, col) in buttons:
            if text == '=':
                button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=self.solve)
            elif text == 'C':
                button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=self.clear)
            else:
                button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: self.show(t))
            button.grid(row=row, column=col, sticky='nsew')

        for i in range(1, 6):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except:
            self.equation.set("Error")
            self.entry_value = ''

if __name__ == '__main__':
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
