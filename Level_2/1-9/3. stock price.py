#2021/01/06

def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices) - 1):
        for j in range(i, len(prices) - 1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1
    return answer

from collections import deque
def solution2(prices):
    answer = []
    prices = deque(prices)

    while prices:
        c = prices.popleft()
        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1
        answer.append(count)
    return answer