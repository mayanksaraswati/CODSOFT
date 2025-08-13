import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == "+":
            res = num1 + num2
        elif op == "-":
            res = num1 - num2
        elif op == "*":
            res = num1 * num2
        elif op == "/":
            if num2 != 0:
                res = num1 / num2
            else:
                res = "Error (Divide by 0)"
        else:
            res = "Invalid"

        result_label.config(text=f"Result: {res}")
    except ValueError:
        result_label.config(text="Error: Enter valid numbers")

# Window setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x200")

# Widgets
tk.Label(root, text="First Number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Operation (+, -, *, /):").pack()
operation = tk.Entry(root)
operation.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=5)
result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()
