# Program Name: AppDevAssignment3.py
# Course: IT3883/Section 01
# Student Name: Mina Bayramoglu
# Assignment Number: Assignment 3
# Due Date: 3/6/2026
#https://medium.com/@amaithichirasan.s/your-first-simple-python-gui-program-miles-to-kilometer-converter-using-tkinter-beginner-level-c8b94e758c2
#https://www.w3schools.com/python/python_try_except.asp
#https://www.tutorialkart.com/python/tkinter/how-to-setup-change-event-for-entry-widget-in-tkinter-python/
import tkinter as tk

def calc(event=None):
    mpg_value = mpg_entry.get()

    try:
        mpg = float(mpg_value)
        km = (mpg * 0.425143707)
        result_var.set(f"{km:.2f}")
    except:
        result_var.set("")

#create GUI
window = tk.Tk()
window.title("MPG to KM/L Converter")
window.geometry("200x100")
#mpg label
mpg_label = tk.Label(window, text="Miles per Gallon (MPG):")
mpg_label.pack(pady=5)
#input
mpg_entry = tk.Entry(window)
mpg_entry.pack()
mpg_entry.bind("<KeyRelease>", calc)

result_text = tk.Label(window, text="Kilometers Per Liter (KM/L):")
result_text.pack(pady=5)

#results
result_var = tk.StringVar()
result_label = tk.Label(window, textvariable=result_var, font=("Arial", 12))
result_label.pack()
window.mainloop()