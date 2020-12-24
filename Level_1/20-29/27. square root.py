#2020/12/24

import math
def solution(n):
    num = math.sqrt(n)
    if math.sqrt(n) == int(math.sqrt(n)) :
        return pow(num + 1, 2)
    return -1

def solution2(n):
    sqrt = n ** (1/2)
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1