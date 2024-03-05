import tkinter as tk

def on_click(button_value):
    current_text = entry_var.get()
    if button_value == '=':
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_value == 'C':
        entry_var.set('')
    else:
        entry_var.set(current_text + button_value)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for input and display
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify='right', font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create and place buttons
row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 12),
              command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the GUI main loop
root.mainloop()
