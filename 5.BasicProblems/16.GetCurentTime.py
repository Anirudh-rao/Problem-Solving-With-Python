import datetime

def DateTimeGenerator():
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time is {time}")


DateTimeGenerator()
DateTimeGenerator()

