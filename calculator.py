import tkinter as tk

# Function to handle button clicks
def button_click(event):
    current_text = result_display.get("1.0", "end-1c")
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            result_display.delete("1.0", tk.END)
            result_display.insert(tk.END, str(result))
        except Exception as e:
            result_display.delete("1.0", tk.END)
            result_display.insert(tk.END, "Error")
    elif button_text == "C":
        result_display.delete("1.0", tk.END)
    else:
        result_display.insert(tk.END, button_text)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create a text display
result_display = tk.Text(window, height=2, width=20, font=("Arial", 20))
result_display.grid(row=0, column=0, columnspan=4)

# Define button labels
button_labels = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create and arrange buttons
row_val = 1
col_val = 0
buttons = []

for button_label in button_labels:
    button = tk.Button(window, text=button_label, padx=20, pady=20, font=("Arial", 20))
    button.grid(row=row_val, column=col_val)
    buttons.append(button)
    col_val += 1

    if col_val > 3:
        col_val = 0
        row_val += 1

# Bind button click event
for button_label, button in zip(button_labels, buttons):
    button.bind("<Button-1>", button_click)

window.mainloop()
