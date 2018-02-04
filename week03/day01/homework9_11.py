from tkinter import *

import time

import math


class CurrentTime:
    def __init__(self):
        window = Tk()
        cavs = Canvas(window, width=300, height=300, bg="white")
        cavs.pack()
        cavs.create_oval(50, 50, 250, 250)
        cavs.create_oval(147, 147, 153, 153,fill="black")
        cavs.create_text(150,45,text="12")
        cavs.create_text(255,150,text="3")
        cavs.create_text(150,255,text="6")
        cavs.create_text(45,150,text="9")
        while True:
            seconds, minutes, hours = self.getCurrentTime()
            sx, sy = self.getMinutesXY(seconds, 90)
            cavs.create_line(150, 150, sx, sy, arrow="last", tag="second")
            mx, my = self.getMinutesXY(minutes, 75)
            cavs.create_line(150, 150, mx, my, arrow="last", tag="minute")
            hx, hy = self.getHoursXY(hours + 8, 60)
            cavs.create_line(150, 150, hx, hy, arrow="last", tag="hour")
            cavs.after(1000)
            cavs.update()
            cavs.delete("second","minute","hour")
        window.mainloop()
        pass

    def getCurrentTime(self):
        totalseconds = int(time.time())
        seconds = totalseconds % 60
        minutes = (totalseconds // 60) % 60
        hours = (totalseconds // (60 * 60)) % 24
        return seconds, minutes, hours
        pass

    def getMinutesXY(self, minutes, r):
        deger = (minutes / 60) * 2 * math.pi
        mx = 150 + r * math.sin(deger)
        my = 150 - r * math.cos(deger)
        return mx, my
    def getHoursXY(self, hours, r):
        deger = (hours % 12)/12 * 2 * math.pi
        hx = 150 + r * math.sin(deger)
        hy = 150 - r * math.cos(deger)
        return hx, hy

    pass


if __name__ == "__main__":
    CurrentTime()
    # print(time.time())
    # totalseconds = int(time.time())
    # seconds = totalseconds % 60
    # minutes = (totalseconds // 60) % 60
    # hours = (totalseconds // (60 * 60)) % 24
    # print(hours,minutes,seconds)

    pass
