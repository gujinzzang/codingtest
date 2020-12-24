#2020/12/24

def solution(arr):
    if len(arr) > 1 :
        arr.pop(arr.index(min(arr)))
        return arr
    else :
        return [-1]

def solution2(arr):
    arr.remove(min(arr))
    return arr