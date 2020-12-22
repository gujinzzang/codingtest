#2020/12/17

def solution(arr, divisor):
    answer = []
    for i in range(len(arr)) :
        if arr[i] % divisor == 0 :
            answer.append(arr[i])
    if len(answer) == 0 :
        answer.append(-1)
    else :
        answer.sort()
    return answer

def solution2(arr, divisor): 
  return sorted([n for n in arr if n % divisor == 0]) or [-1]