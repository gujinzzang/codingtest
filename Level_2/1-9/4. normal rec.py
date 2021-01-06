#2021/01/06

from math import gcd
def solution(w,h):
    return (w * h) - (w + h - gcd(w, h))