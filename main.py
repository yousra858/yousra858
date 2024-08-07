from tkinter import *
from time import sleep

my_tk = Tk()
my_tk.config(padx=100, pady=100, bg="#E0A75E")

my_canvas = Canvas(width=270, height=300, bg="#E0A75E", highlightthickness=0)
my_label = Label(text="Welcome", font=("Courier", 30, "bold"), bg="#E0A75E")

image1 = PhotoImage(file="apple-95-270x300.png")

my_canvas.create_image(135, 150, image=image1)
canvas_time = my_canvas.create_text(135, 150, text="00,00", font=("Courier", 30, "bold"), fill="white")
my_canvas.grid(row=0, column=1)
watch = True
sleep(0)


def stop_watch(x):
    global watch
    if watch == True:
        my_canvas.itemconfig(canvas_time, text=x)
        my_tk.after(1000, stop_watch, x + 1)

def start():
    global watch
    watch = True
    stop_watch(0)


def stop_button():
    global watch
    watch = False


my_button = Button(text='start', font=('Courier', 20, 'bold'), command=start)
my_button.grid(column=0, row=3)
my_button.config(padx=10, pady=10)

my_button1 = Button(text='stop', font=('Courier', 20, 'bold'), command=stop_button)
my_button1.grid(column=2, row=3)
my_button1.config(padx=10, pady=10)

my_tk.mainloop()
