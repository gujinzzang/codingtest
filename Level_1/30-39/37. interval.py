#2020/12/28

def solution(x, n):
    return [i * x + x for i in range(n)]

def solution2(x, n):
    answer = list(range(x, n * x + 1, x))
    return answer