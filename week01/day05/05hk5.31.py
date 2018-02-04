# 判断该年是否为闰年

def isRunYears(year):
    if ((year % 4 == 0) and (not year % 100 == 0)) or (year % 400 == 0):
        return True
    else:
        return False

MonthList = ["January","February","March","April","May","June","July",
             "August","September","October","November","December"]
years = eval(input("请输入年份："))
week = eval(input("请输入该年第一天为："))
weekDaysList = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
monthOf31List = [1, 3, 5, 7, 8, 10, 12]
monthOf30List = [4, 6, 9, 11]
monthOfDays = 0
yearOfDays = 365 if isRunYears(years) else 366
for i in range(12):
    print("%d月的一天为：%s" % (i + 1, weekDaysList[week-1]))
    if (monthOf31List.count(i+1) == 1):
        monthOfDays = 31
        # print(i,monthOfDays)
    elif (monthOf30List.count(i+1) == 1):
        monthOfDays = 30
    else:
        if (isRunYears(years)):
            monthOfDays = 29
        else:
            monthOfDays = 28
            pass
    week = (week+monthOfDays)%7

def calender (year,month,FirstDay):
    global MonthList
    print(format(MonthList[month]+" "+str(year),"^40s"))
    print("---------------------------------------------")
    pass

calender(2015,1,"222")