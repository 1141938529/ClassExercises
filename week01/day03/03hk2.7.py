# 2.7
minutes = eval(input("enter the number of minutes:"))
years = minutes // (365 * 24 * 60)
day = (minutes % (365 * 24 * 60)) // (24 * 60)
print("%d mintues is approximate %d years and %d days"
      % (minutes, years, day))
