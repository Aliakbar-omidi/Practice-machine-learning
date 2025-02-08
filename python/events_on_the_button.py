
from tkinter import messagebox as msg
from tkinter import Tk, Button, Label


def hover(event):
    msg.showinfo('Hover', "Button is hovered")


def click(event):
    msg.showinfo('Click', "Button is clicked")


def key_press(event):
    msg.showinfo('Key Press', f"کمه ی {event.char} فشرده شد")


window = Tk()
window.geometry('300x200')
window.title("Event On The Button")

Label(window, text="درصورت فشرده شدن کلیدی اون نمایش داده میشه")

btn1 = Button(window, text="for hover")
btn1.pack(padx=5, pady=20)

btn2 = Button(window, text="Hello")
btn2.pack(padx=5, pady=20)

btn1.bind("<Enter>", hover)
btn2.bind("<Button-1>", click)

window.bind("<Key>", key_press)

window.mainloop()
