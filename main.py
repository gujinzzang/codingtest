###coding test

#middle letter
def solution1(s):
    p = len(s) // 2
    if len(s) % 2 == 0:
        return str[p-1:p+1]
    else:
        return str[p]

#complete race
import collections

def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

#Kth number
def solution3(array, commands):
    answer = []
    for i in commands:
        answer.append(sorted(array[i[0]-1:i[1]])[i[2]-1])
    return answer

def solution3_1(array, commands):
    return list(map(lambda x : sorted(array[x[0]-1:x[1]])[x[2]-1],commands))

