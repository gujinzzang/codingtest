#2020/12/23

def solution(n):
	result = 0
	for i in str(n):
		result += int(i)
	return result

def solution2(n):
    return sum([int(i) for i in str(n)])