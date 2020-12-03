#2020/11/30

def solution1(s):
    p = len(s) // 2
    if len(s) % 2 == 0:
        return str[p-1:p+1]
    else:
        return str[p]