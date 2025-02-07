
from tkinter import Tk, Label, Button, Entry, messagebox

pi = 3.14


def circle_area():
    try:
        radius = float(entry_radius.get())
        area = pi * radius * radius
        messagebox.showinfo("Circle Area", f"مساحت دایره: {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "لطفاً یک مقدار عددی معتبر وارد کنید")


window = Tk()
window.geometry("400x200")
window.title("محاسبه مساحت دایره")

Label(window, text="شعاع را وارد کنید").pack(pady=10)
entry_radius = Entry(window)
entry_radius.pack(pady=5)

btn = Button(window, text="محاسبه", command=circle_area, bg="white", fg="black")
btn.pack(pady=10)


window.mainloop()
