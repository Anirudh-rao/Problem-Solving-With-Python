import calendar


def CalenderGenerator():
    y = int(input("Input the year:"))
    m = int(input("Input the Month:"))    
    print(calendar.month(y,m))

CalenderGenerator()
CalenderGenerator()