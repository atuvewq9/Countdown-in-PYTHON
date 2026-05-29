from tkinter import *

def countdown():
    global t

    if t >= 0:
        seconds = t % 60
        minutes = (t // 60) % 60
        hours = t // 3600

        label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")

        t -= 1

        window.after(1000, countdown)
    else:
         label.config(text="TIME UP!")


def start_timer():
    global t
    t = int(entry.get())
    countdown()


window = Tk ()
window.title("Countdown Timer")
window.geometry("300x200")

title = Label(window, text="Countdown Timer", font=("Arial", 50),compound=TOP)
title.place(x=870,y=20)

entry =Entry(window, font=("Arial", 35))
entry.place(x=870,y=400)

button = Button(window, text="Start", command=start_timer,font=("Arial",35),fg="white",bg="red")
button.place(x=1000,y=500)


label = Label(window, text="00:00:00", font=("Arial", 35))
label.place(x=470,y=500)
window.mainloop()
