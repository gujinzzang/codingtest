#2020/12/15

def solution(n): 
    return ('수박' * n) [0:n]

def solution2(n): 
    answer = '' 
    for i in range(n): 
        if i % 2 == 0: 
            answer += '수' 
        else: answer += '박' 
    return answer