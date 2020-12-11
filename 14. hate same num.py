#2020/12/10

def solution(arr):    
    answer = []
    for i in arr:
        if len(answer) == 0 :
            answer.append(i)
            continue
        if(answer[-1] != i) :
            answer.append(i)
    return answer

def solution2(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]: continue
        answer.append(i)
    return answer