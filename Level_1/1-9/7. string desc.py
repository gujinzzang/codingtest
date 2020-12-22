#2020/12/03

def solution(s):
    return ''.join(sorted(s, reverse=True))

def solution2(s):
    return (''.join(sorted(s)[::-1]))