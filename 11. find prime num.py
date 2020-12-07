#2020/12/07

def solution(n):
    sum = 0
    s = 0
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                s += 1
        if s == 0:
            sum += 1
        s = 0
    return sum

def solution2(n):
    num = set(range(2, n+1))
    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)