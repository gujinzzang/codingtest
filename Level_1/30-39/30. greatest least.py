#2020/12/24

from fractions import gcd
def solution(n, m):
    return [gcd(n, m), n * m / gcd(n, m)]