import tkinter as tk
from calculator import Calculator

class CalculatorApp:
    def __init__(self, root):
        self.calc = Calculator()
        self.root = root
        self.root.title("OOP Calculator")

        self.entry1 = tk.Entry(root)
        self.entry2 = tk.Entry(root)
        self.result = tk.Label(root, text="Result: ")

        self.entry1.pack()
        self.entry2.pack()

        tk.Button(root, text="Add", command=self.add).pack()
        tk.Button(root, text="Subtract", command=self.subtract).pack()
        tk.Button(root, text="Multiply", command=self.multiply).pack()
        tk.Button(root, text="Divide", command=self.divide).pack()

        self.result.pack()

    def get_inputs(self):
        try:
            return float(self.entry1.get()), float(self.entry2.get())
        except ValueError:
            return 0, 0

    def add(self):
        a, b = self.get_inputs()
        self.result.config(text=f"Result: {self.calc.add(a, b)}")

    def subtract(self):
        a, b = self.get_inputs()
        self.result.config(text=f"Result: {self.calc.subtract(a, b)}")

    def multiply(self):
        a, b = self.get_inputs()
        self.result.config(text=f"Result: {self.calc.multiply(a, b)}")

    def divide(self):
        a, b = self.get_inputs()
        self.result.config(text=f"Result: {self.calc.divide(a, b)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
