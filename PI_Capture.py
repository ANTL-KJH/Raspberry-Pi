"""
* Project : Raspberry PI Capture
* Program Purpose and Features :
* - service 2 mode Capture program [full/window]
* Author : JH KIM
* First Write Date : 2023.11.13
* ==========================================================================
* Program history
* ==========================================================================
* Author    		Date		    Version		History
* JH KIM            2023.11.13      v1.00       First Write

"""
import tkinter
import subprocess
import os
from datetime import datetime


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except:
        return


def capFullScreen():
    now = datetime.now()
    s = "/home/pi/KJH_Capture/"
    d = now.date()
    t = now.time()
    s += str(d) + "_" + str(t.hour) + str(t.minute) + str(t.second) + ".png"
    subprocess.call(["scrot", s])


def capWindowScreen():
    now = datetime.now()
    s = "/home/pi/KJH_Capture/"
    d = now.date()
    t = now.time()
    s += str(d) + "_" + str(t.hour) + str(t.minute) + str(t.second) + ".png"
    subprocess.call(["scrot", "-s", s])


def main():
    createDirectory("/home/pi/KJH_Capture")
    top = tkinter.Tk()
    top.title("PI Screen Shot")
    top.geometry("300x150")

    B = tkinter.Button(top, text="Full Screen Capture", width=50, command=capFullScreen)
    B.pack()
    B = tkinter.Button(top, text="Window Capture", width=50, command=capWindowScreen)
    B.pack()
    B = tkinter.Button(top, text="Exit", width=50, command=exit)
    B.pack()

    top.mainloop()


if __name__ == "__main__":
    main()
