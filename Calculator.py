import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.entry = tk.Entry(root, width=20, font=('Helvetica', 20))
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button_text in buttons:
            tk.Button(root, text=button_text, width=5, height=2, command=lambda text=button_text: self.on_button_click(text)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button_text):
        if button_text == 'C':
            self.entry.delete(0, tk.END)
        elif button_text == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, button_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
