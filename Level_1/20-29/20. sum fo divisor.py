#2020/12/21

def solution(num): 
    answer = 0 
    for i in range(1,num + 1): 
        if num % i==0: 
            answer += i 
    return answer

def solution2(num):
  return sum([i for i in range(1, num + 1) if num % i == 0])