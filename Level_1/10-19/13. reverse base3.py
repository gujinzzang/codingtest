#2020/12/14

def solution(n):
    n3 = []
    while n > 0:
        n3.append(n % 3)
        n //= 3
    answer = 0
    for i in range(len(n3)):
        answer *= 3
        answer += n3[i]
    return answer

import math
def solution2(n):
    list = []
    answer = 0
    while n > 0 :
        list.insert(0,n % 3)
        n = math.floor(n / 3)
    stnd = 1
    for i in list :
        answer += i * stnd
        stnd = stnd * 3
    
    return answer