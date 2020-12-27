#2020/12/28

def solution(arr1, arr2):
    answer = [] 
    for i in range(len(arr1)): 
        tmp=[] 
        for j in range(len(arr1[i])): 
            tmp.append(arr1[i][j]+arr2[i][j]) 
        answer.append(tmp) 
    return answer

import numpy as np
def solution2(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    answer = arr1 + arr2
    return answer.tolist()