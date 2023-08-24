import random
import math
import time
import datetime


def test_randomno():
    x = 100
    y = 500
    z = 10

    print(random.randrange(x, y, z))
    print(random.randrange(3, 9))


def test_math():
    x = -6654.896
    y = 6

    print(math.ceil(x))
    print(math.floor(x))
    print(math.fabs(x))
    print(math.factorial(y))


def test_date():
    print(time.gmtime())
    print(time.localtime())
    print(time.strftime("%S:%H:%M"))
    print(datetime.date.today())
    print(datetime.date.today().strftime("%d"))