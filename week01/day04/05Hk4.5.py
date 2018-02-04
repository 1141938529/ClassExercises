today = eval(input("enter today's day:"))
future = eval(input("enter the number of days elapsed since "
                    "today:"))
def Weeks(day):

    if (day == 0):
        return "Sunday"
        pass
    elif (day == 1):
        return "Monday"
        pass
    elif (day == 2):
        return "Tuesday"
        pass
    elif (day == 3):
        return "Wednesday"
        pass
    elif (day == 4):
        return "Thursday"
        pass
    elif (day == 5):
        return "Friday"
        pass
    elif (day == 6):
        return "Saturday"
        pass
print("today is %s and the future day is %s"
      %(Weeks(today),Weeks((future+today)%7)))