from tkinter import *
import tkinter

screen = Tk()
screen.title("My GUI")
screen.geometry("600x600")
screen.configure(background="Gray")

frame_enabled = False


def toggle_frame():
    global frame_enabled
    if not frame_enabled:
        my_frame.pack(fill='both', expand=True)
    else:
        my_frame.pack_forget()
    frame_enabled = not frame_enabled


button1 = Button(screen, text="Toggle frame", command=toggle_frame)
button1.pack()

my_frame = Frame(screen, bg="red")
screen.mainloop()