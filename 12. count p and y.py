#2020/12/08

def solution(s):
    a = 0
    b = 0
    for i in s:
        if i == "p" or i == "P":
            a += 1
        elif i == "y" or i == "Y":
            b += 1
    if a == b:
        return True
    else:
        return False
    return True 

def solution2(s):
    return s.lower().count("p") == s.lower().count("y")