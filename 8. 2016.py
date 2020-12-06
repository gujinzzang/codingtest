#2020/12/06

import datetime

def solution(a, b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]

from datetime import date
def solution2(a, b):
    return date(2016,a,b).strftime('%a').upper()