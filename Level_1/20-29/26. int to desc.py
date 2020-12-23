#2020/12/23

def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

def solution2(n):
    return int("".join(sorted(list(str(n)), reverse=True)));