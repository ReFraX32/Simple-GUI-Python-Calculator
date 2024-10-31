import tkinter as tk
from tkinter import ttk

field_text = ""

def add_to_field(sth):
    global field_text
    field_text += str(sth)
    field.delete("1.0", "end")
    field.insert("1.0", field_text)

def calculate():
    global field_text
    try:
        result = str(eval(field_text))
        field.delete("1.0", "end")
        field.insert("1.0", result)
        field_text = result
    except Exception as e:
        field.delete("1.0", "end")
        field.insert("1.0", "Error")

def clear():
    global field_text
    field_text = ""
    field.delete("1.0", "end")

def delete():
    global field_text
    field_text = field_text[:-1]
    field.delete("1.0", "end")
    field.insert("1.0", field_text)

# Handle mouse hover effect
def on_hover(button):
    original_color = button.cget("bg")
    if original_color == "grey10":
        button.config(bg="grey20")
    elif original_color == "Royal Blue4":
        button.config(bg="Royal Blue3")
    elif original_color == "dark red":
        button.config(bg="red3")
    elif original_color == "dark green":
        button.config(bg="green3")
    elif original_color == "Royal Blue1":
        button.config(bg="blue")

# Handle mouse leave effect
def on_leave(button):
    original_color = button._original_color
    button.config(bg=original_color)

def button_blueprint(textbox, value, bg_color, fg_color="white"):
    buttonbox = tk.Button(window, text=textbox, command=lambda: add_to_field(value), 
                         width=5, font=("Times New Roman", 14), 
                         bg=bg_color, fg=fg_color,
                         relief="raised",
                         borderwidth=0)
    # Store original color for hover effect
    buttonbox._original_color = bg_color
    
    # Add hover effects
    buttonbox.bind("<Enter>", lambda e: on_hover(buttonbox))
    buttonbox.bind("<Leave>", lambda e: on_leave(buttonbox))
    
    # Add rounded corners
    buttonbox.config(relief="flat")
    return buttonbox

def handle_keypress(event):
    # Handle keyboard input
    key = event.char
    
    # Handle numeric keys and operators
    if key in "0123456789+-*/.()":
        add_to_field(key)
    # Handle enter/return key as equals
    elif event.keysym in ["Return", "KP_Enter"]:
        calculate()
    # Handle backspace
    elif event.keysym == "BackSpace":
        delete()
    # Handle escape key as clear
    elif event.keysym == "Escape":
        clear()

# Tkinter Window Configuration
window = tk.Tk()
window.geometry("300x300")
window.resizable(0,0)
window.title("Simple Calculator")
window.configure(bg="grey5")

# Bind keyboard events
window.bind("<Key>", handle_keypress)

# Text Field configuration
field = tk.Text(window, height=2, width=21, font=("Times New Roman", 20), 
                bg="grey20", fg="white",
                relief="flat",
                borderwidth=0)
field.grid(row=1, column=1, columnspan=4, padx=5, pady=5)

# Number Buttons
btn_1 = button_blueprint("1", 1, "grey10")
btn_1.grid(row=5, column=1, padx=2, pady=2)

btn_2 = button_blueprint("2", 2, "grey10")
btn_2.grid(row=5, column=2, padx=2, pady=2)

btn_3 = button_blueprint("3", 3, "grey10")
btn_3.grid(row=5, column=3, padx=2, pady=2)

btn_4 = button_blueprint("4", 4, "grey10")
btn_4.grid(row=4, column=1, padx=2, pady=2)

btn_5 = button_blueprint("5", 5, "grey10")
btn_5.grid(row=4, column=2, padx=2, pady=2)

btn_6 = button_blueprint("6", 6, "grey10")
btn_6.grid(row=4, column=3, padx=2, pady=2)

btn_7 = button_blueprint("7", 7, "grey10")
btn_7.grid(row=3, column=1, padx=2, pady=2)

btn_8 = button_blueprint("8", 8, "grey10")
btn_8.grid(row=3, column=2, padx=2, pady=2)

btn_9 = button_blueprint("9", 9, "grey10")
btn_9.grid(row=3, column=3, padx=2, pady=2)

btn_0 = button_blueprint("0", 0, "grey10")
btn_0.grid(row=6, column=1, padx=2, pady=2)

btn_dot = button_blueprint(".", ".", "grey10")
btn_dot.grid(row=6, column=2, padx=2, pady=2)

# Operation Buttons
btn_plus = button_blueprint("+", "+", "Royal Blue4")
btn_plus.grid(row=5, column=4, padx=2, pady=2)

btn_minus = button_blueprint("-", "-", "Royal Blue4")
btn_minus.grid(row=4, column=4, padx=2, pady=2)

btn_multiply = button_blueprint("*", "*", "Royal Blue4")
btn_multiply.grid(row=3, column=4, padx=2, pady=2)

btn_divide = button_blueprint("/", "/", "Royal Blue4")
btn_divide.grid(row=2, column=4, padx=2, pady=2)

btn_open_parenthesis = button_blueprint("(", "(", "Royal Blue4")
btn_open_parenthesis.grid(row=2, column=2, padx=2, pady=2)

btn_close_parenthesis = button_blueprint(")", ")", "Royal Blue4")
btn_close_parenthesis.grid(row=2, column=3, padx=2, pady=2)

# Special Buttons with hover effects
btn_equal = tk.Button(window, text="=", command=calculate, 
                     width=5, font=("Times New Roman", 14), 
                     bg="Royal Blue1", fg="white",
                     relief="flat", borderwidth=0)
btn_equal._original_color = "Royal Blue1"
btn_equal.bind("<Enter>", lambda e: on_hover(btn_equal))
btn_equal.bind("<Leave>", lambda e: on_leave(btn_equal))
btn_equal.grid(row=6, column=4, padx=2, pady=2)

btn_del = tk.Button(window, text="DEL", command=delete, 
                   width=5, font=("Times New Roman", 14), 
                   bg="dark red", fg="white",
                   relief="flat", borderwidth=0)
btn_del._original_color = "dark red"
btn_del.bind("<Enter>", lambda e: on_hover(btn_del))
btn_del.bind("<Leave>", lambda e: on_leave(btn_del))
btn_del.grid(row=6, column=3, padx=2, pady=2)

btn_clear = tk.Button(window, text="AC", command=clear, 
                     width=5, font=("Times New Roman", 14), 
                     bg="dark green", fg="white",
                     relief="flat", borderwidth=0)
btn_clear._original_color = "dark green"
btn_clear.bind("<Enter>", lambda e: on_hover(btn_clear))
btn_clear.bind("<Leave>", lambda e: on_leave(btn_clear))
btn_clear.grid(row=2, column=1, padx=2, pady=2)

# App Loop
window.mainloop()
