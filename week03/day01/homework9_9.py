from tkinter import *


class Barchart:
    def __init__(self):
        window = Tk()
        window.title("Bar Chart")
        canvas = Canvas(window, width=500, height=300,bg="white")
        canvas.create_line(5,250,495,250,width=3)
        canvas.create_rectangle(10,250,110,150,fill="red")
        canvas.create_rectangle(130,250,230,200,fill="blue")
        canvas.create_rectangle(250,250,350,100,fill="green")
        canvas.create_rectangle(370,250,470,50,fill="orange")
        canvas.create_text(60,143,text="课题--20%")
        canvas.create_text(180,193,text="测试--10%")
        canvas.create_text(300,93,text="期中考试--30%")
        canvas.create_text(420,43,text="期末考试--40%")
        canvas.pack()
        window.mainloop()

    pass
if __name__ == "__main__":
    Barchart()