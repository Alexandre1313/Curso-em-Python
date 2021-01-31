import datetime

def calc_(h1, m1, h2, m2):
    hor1 = datetime.timedelta(hours=h1, minutes=m1)
    hor2 = datetime.timedelta(hours=h2, minutes=m2)
    r = hor2 - hor1
    print(r)


h1 = int(input('hours1: '))
m1 = int(input('minutes1: '))
h2 = int(input('hours2: '))
m2 = int(input('minutes2: '))
calc_(h1, m1, h2, m2)
