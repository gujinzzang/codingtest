#2020/12/09

def solution(s):
    return int(s)

def solution2(s):
    head = s[0]
    if head.isdigit():
        return int(s)
    else:
        if head == "+":
            return int(s[1:])
        else:
            return -1 * int(s[1:])