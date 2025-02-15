from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title('Calculator')
        master.geometry('357x420+0+0')
        master.config(bg='#f4f4f9')  # Light off-white background
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(master, width=22, bg='#dfe4ea', fg='black', font=('Arial', 22), textvariable=self.equation, justify='right', bd=5, relief='ridge').place(x=0, y=0)

        buttons = [
            ('(', 0, 50, '#a4b0be'), (')', 90, 50, '#a4b0be'), ('%', 180, 50, '#ffb142'), ('/', 270, 50, '#ffb142'),
            ('7', 0, 125, '#ffffff'), ('8', 90, 125, '#ffffff'), ('9', 180, 125, '#ffffff'), ('*', 270, 125, '#ffb142'),
            ('4', 0, 200, '#ffffff'), ('5', 90, 200, '#ffffff'), ('6', 180, 200, '#ffffff'), ('-', 270, 200, '#ffb142'),
            ('1', 0, 275, '#ffffff'), ('2', 90, 275, '#ffffff'), ('3', 180, 275, '#ffffff'), ('+', 270, 275, '#ffb142'),
            ('C', 0, 350, '#e74c3c'), ('0', 90, 350, '#ffffff'), ('.', 180, 350, '#ffffff'), ('=', 270, 350, '#1dd1a1')
        ]

        for (text, x, y, color) in buttons:
            Button(master, width=10, height=3, text=text, relief='flat',
                   bg=color, fg='black' if text not in ['=', 'C'] else 'white',
                   font=('Arial', 14, 'bold'),
                   command=lambda t=text: self.show(t) if t not in ['=', 'C'] else (self.solve() if t == '=' else self.clear())
                   ).place(x=x, y=y)

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
        except:
            self.equation.set("Syntax Error")
            self.entry_value = ''


root = Tk()
calculator = Calculator(root)
root.mainloop()
