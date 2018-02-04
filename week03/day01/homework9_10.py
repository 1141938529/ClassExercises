from tkinter import Canvas, Tk
from math import pow

class Piechart :
    def __init__(self):
        window = Tk()
        window.title("Pie Chart")
        cavs = Canvas(window,width=300,height=300,bg="white")
        cavs.create_arc(50,50,250,250,start=0,extent=72,fill="red")
        cavs.create_arc(50,50,250,250,start=72,extent=36,fill="blue")
        cavs.create_arc(50,50,250,250,start=108,extent=108,fill="green")
        cavs.create_arc(50,50,250,250,start=216,extent=144,fill="yellow")
        cavs.create_text(65,130,text="期中考试--30%")
        cavs.create_text(200,230,text="期末考试--40%")
        cavs.create_text(160,40,text="测试--10%")
        cavs.create_text(265,90,text="课题--20%")
        cavs.pack()
        window.mainloop()
    pass
if __name__ =="__main__":
    Piechart()