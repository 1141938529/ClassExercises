from tkinter import *

def myMouseEvent(event):
    print("当前位置：",event.x_root,event.y_root)
    pass
def myKeyEvent(event):
    print("当前位置：",event.char,event.keycode)
    pass

window = Tk()
pimg = PhotoImage(file="../res/img/b12.gif",height=400,width=400)
label = Label(window, image=pimg)
label.pack()
label.focus_set()
label.bind(sequence="<Button-3>",func=myMouseEvent)
label.bind(sequence="<Key>",func=myKeyEvent)
window.mainloop()