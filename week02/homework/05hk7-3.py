class Account:
    __id = 0000
    __balance = 0.0
    __annualInterestRate = 0.0

    def __init__(self, id1=0, balance=100, annual=0):
        self.__id = id1
        self.__balance = balance
        self.__annualInterestRate = annual
        pass

    def getID(self):
        return self.__id

    def setID(self, id1):
        self.__id = id1

    def getbalance(self):
        return self.__balance

    def setbalance(self, banlance):
        self.__balance = banlance

    def getannualInterestRate(self):
        return self.__annualInterestRate

    def setannualInterestRate(self, annual):
        self.__annualInterestRate = annual

    def getMonthlyRate(self):
        return self.__annualInterestRate / 12/100

    def getMonthlyIterest(self):
        return self.__balance * self.getMonthlyRate()

    def withdraw(self, money):
        self.__balance -= money

    def deposit(self, money):
        self.__balance += money

    pass

if __name__ == "__main__":
    myAcount = Account(1122,20000,4.5)
    myAcount.withdraw(2500)
    myAcount.deposit(3000)
    print("ID为：%d，账户额为：%.2f，月利率为：%.6f，月利息为%.2f"
          %(myAcount.getID(),myAcount.getbalance(),myAcount.getMonthlyRate(),myAcount.getMonthlyIterest()))
