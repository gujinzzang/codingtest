#2020/12/31

def solution(priorities, location):
    array1 = [c for c in range(len(priorities))]
    array2 = priorities.copy()
    i = 0

    while True:
        if array2[i] < max(array2[i + 1:]):
            array1.append(array1.pop(i))
            array2.append(array2.pop(i))
        else:
            i += 1
        if array2 == sorted(array2, reverse = True):
            break

    return array1.index(location) + 1

def solution2(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer