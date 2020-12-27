#2020/12/28

def solution(num):
    if num == 1 :
        return 0
    for i in range(500) :
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        if num == 1 :
            return i + 1
    return -1

def solution2(num):
    answer = 0
    while num!=1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
        answer = answer + 1
        if answer >= 500:
            return -1
    return answer