#2020/12/28

def solution(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    if x % sum == 0:
        return True
    else:
        return False

def solution2(x):
    return x % sum([int(c) for c in str(x)]) == 0