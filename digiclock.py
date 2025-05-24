import tkinter as tk
from time import strftime

root = tk.Tk()
root.title('***DIGITAL CLOCK***')

def time():
    string = strftime('%H:%M:%S %p\n %D')  # Get current time and date
    label.config(text=string)  # Update the label's text
    label.after(1000, time)  # Call the time function every 1000ms (1 second)

label = tk.Label(root, font=('calibri', 50, 'bold'), bg='yellow',fg='black',height=100,width=100)  # Define the label
label.pack(anchor='center')  # Place the label in the window

time()  # Start the clock

root.mainloop()  # Start the GUI loop