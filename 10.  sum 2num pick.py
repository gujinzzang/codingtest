#2020/12/07

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            out = numbers[i] + numbers[j]
            if not out in answer:
                answer.append(out)
    answer.sort()    
    return answer

from itertools import combinations

def solution2(numbers):
    answer = []
    l = list(combinations(numbers, 2))

    for i in l:
        answer.append(i[0]+i[1])
    answer = list(set(answer))
    answer.sort()

    return answer