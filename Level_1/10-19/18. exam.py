#2020/12/21

def solution(answers):
    answer = []
    score = [0, 0, 0]
    patern1 = [1, 2, 3, 4, 5]
    patern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    patern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)): 
        if answers[i] == patern1[i % len(patern1)]:
            score[0] += 1
        if answers[i] == patern2[i % len(patern2)]:
            score[1] += 1
        if answers[i] == patern3[i % len(patern3)]:
            score[2] += 1
    for person, x in enumerate(score):
        if x == max(score):
            answer.append(person+1)
    return answer

def solution2(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]