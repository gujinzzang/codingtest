#2020/12/22

def solution(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] * b[i])
    return sum(c)

def solution2(a, b):
    return sum(i*j for i,j in zip(a,b))