#2020/12/06

def solution(n, lost, reserve):
    answer = 0 
    answer = n - len(lost)
    for i in lost:
        if reserve.count(i) > 0:
            reserve.remove(i)
            answer += 1
        elif reserve.count(i-1) > 0:
            reserve.remove(i-1)
            answer += 1
        elif reserve.count(i+1) > 0:
            reserve.remove(i+1)
            answer += 1
    return answer

def solution2(n, lost, reserve): 
    reser_del = set(reserve)-set(lost) 
    lost_del = set(lost)-set(reserve) 
    for i in reser_del: 
        if i-1 in lost_del: 
            lost_del.remove(i-1) 
        elif i+1 in lost_del: 
            lost_del.remove(i+1) 
    return n-len(lost_del)