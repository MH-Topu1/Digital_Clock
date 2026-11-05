import tkinter as tk
from time import strftime

window = tk.Tk()
window.title("Digital Clock V2")
window.geometry("500x300")
window.configure(bg="black")

# Current Theme
dark_mode = True

# Time Update Function
def time():
    current_time = strftime('%I:%M:%S %p')
    current_date = strftime('%A, %d %B %Y')

    time_label.config(text=current_time)
    date_label.config(text=current_date)

    window.after(1000, time)

# Theme Change Function
def change_theme():
    global dark_mode

    if dark_mode:
        window.config(bg="white")
        time_label.config(bg="white", fg="black")
        date_label.config(bg="white", fg="black")
        theme_button.config(text="Dark Mode")
        dark_mode = False

    else:
        window.config(bg="black")
        time_label.config(bg="black", fg="white")
        date_label.config(bg="black", fg="white")
        theme_button.config(text="Light Mode")
        dark_mode = True

# Time Label
time_label = tk.Label(
    window,
    font=("calibri", 40, "bold"),
    bg="black",
    fg="white"
)
time_label.pack(pady=20)

# Date Label
date_label = tk.Label(
    window,
    font=("calibri", 18),
    bg="black",
    fg="white"
)
date_label.pack(pady=10)

# Theme Button
theme_button = tk.Button(
    window,
    text="Light Mode",
    font=("calibri", 14),
    command=change_theme
)
theme_button.pack(pady=20)

# Start Clock
time()

# Run Window
window.mainloop()
