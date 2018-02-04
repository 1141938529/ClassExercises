from tkinter import *

def text1():
    window = Tk()
    lab = Label(window, text="welcome to python")
    btn = Button(window, text="Click me")
    btn.pack()
    lab.pack()

    window.mainloop()

def text2():
    window = Tk()
    IntVar()
    btn1 = Button(window,text ="Click",bg="red",command=btn1Click )
    btn1.pack()
    window.mainloop()


def btn1Click():
    print("i'm ok")

if __name__ == "__main__" :
    # text1()
    text2()