
from tkinter import messagebox as msg

if msg.askyesno("Question", "Are you over 18 years old?"):
    msg.askyesno("Nationality", "Are you from iran?")
    msg.showinfo("welcome", "your welcome message")
else:
    msg.showinfo("bye", "good luck")
