#2021/01/08

import functools

def comparator(a,b):
    x = a + b
    y = b + a
    return (int(x) > int(y)) - (int(x) < int(y))

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key = functools.cmp_to_key(comparator),reverse = True)
    answer = str(int(''.join(n)))
    return answer

def solution2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse = True)
    return str(int(''.join(numbers)))