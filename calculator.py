import tkinter as tk
#----------------------------------------------------------------
# Create main window
root = tk.Tk()
root.title("Cute Calculator")
root.geometry("350x500")  # Adjusted size for a compact design
root.configure(bg="#FFC0CB")  # Light pink background

#----------------------------------------------------------------
# Define colors
button_bg = "#FF69B4"  # Hot pink
button_fg = "white"
display_bg = "#FFB6C1"  # Light pink for display
display_fg = "black"

#----------------------------------------------------------------
## Create a display screen
display = tk.Entry(root, font=("Arial", 20), bg=display_bg, fg=display_fg, bd=10, relief="flat", justify="right")
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)

#----------------------------------------------------------------
# Function to handle button clicks
def on_click(value):
    if value == "=":
        try:
            result = eval(display.get())  # Evaluate the expression
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif value == "C":
        display.delete(0, tk.END)  # Clear display
    else:
        display.insert(tk.END, value)  # Insert clicked button value

#----------------------------------------------------------------
# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("C", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
    ("%", 5, 0), ("(", 5, 1), (")", 5, 2), ("/", 5, 3)  
    # Clear button (row 5, column 0)
]

#----------------------------------------------------------------
# Function to create buttons
for text, row, col in buttons:
    btn = tk.Button(root, text=text, font=("Arial", 15), bg=button_bg, fg=button_fg,
                    width=5, height=2, bd=4, relief="raised", cursor="hand2",
                    command=lambda t=text: on_click(t))  # Make button clickable
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

#----------------------------------------------------------------
# Run the GUI
root.mainloop()