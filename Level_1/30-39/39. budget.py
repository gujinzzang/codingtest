#2020/12/28

def solution(d, budget):
    d.sort()
    answer = 0
    for value in d:
        if value <= budget:
            budget -= value
            answer += 1
    return answer

def solution2(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)