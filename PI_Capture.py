import Tkinter
import subprocess

top = Tkinter.Tk()
top.title("PI Screen Shot")
top.geometry("300x150")


def capFullScreen():
    subprocess.call(["scrot"])


def capWindowScreen():
    subprocess.call(["scrot", "-s"])


B = Tkinter.Button(top, text="Full Screen Capture", width=50, command=capFullScreen)
B.pack()
B = Tkinter.Button(top, text="Window Capture", width=50, command=capWindowScreen)
B.pack()

top.mainloop()
