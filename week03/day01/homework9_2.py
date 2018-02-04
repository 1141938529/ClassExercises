from tkinter import *


class InvestmentValue:
    def __init__(self):
        window = Tk()
        frame = Frame(window)
        Label(frame, text="投资额：").grid(row=1, column=1)
        Label(frame, text="years：").grid(row=2, column=1)
        Label(frame, text="年利率：").grid(row=3, column=1)
        Label(frame, text="未来总额：").grid(row=4, column=1)
        self.entext1 = IntVar()
        self.entext2 = IntVar()
        self.entext3 = IntVar()
        self.entext4 = IntVar()
        Entry(frame, textvariable=self.entext1,justify="right").grid(row=1, column=2)
        Entry(frame, textvariable=self.entext2,justify="right").grid(row=2, column=2)
        Entry(frame, textvariable=self.entext3,justify="right").grid(row=3, column=2)
        Entry(frame, textvariable=self.entext4,justify="right").grid(row=4, column=2)

        Button(frame, text="Calculate", command=self.handleBtnEvent).grid(row=5, column=2, sticky="E")
        frame.pack()
        window.mainloop()

    def handleBtnEvent(self):
        value = self.entext1.get() * ((1 + self.entext3.get()/100/12) ** (self.entext2.get() * 12))
        self.entext4.set(round(value,2))


if __name__ == "__main__":
    InvestmentValue()
