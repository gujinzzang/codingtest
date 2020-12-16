#2020/12/16

def solution(strings, n):
    return sorted(sorted(strings), key = lambda strings: strings[n])

import operator
def solution2(strings, n):
    return sorted(strings, key = operator.itemgetter(n)) 

def solution3(strings, n):
    answer = []
    for i in "abcdefghijklmnopqrstuvwxyz":
        for j in strings:
            if j[n] == i: answer.append(j)
    return answer