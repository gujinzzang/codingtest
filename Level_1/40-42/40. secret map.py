#2020/12/28

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        result = bin(arr1[i] | arr2[i])[2:]
        if len(result) < n:
            result = '0' * (n - len(result)) + result
        str = ''
        for x in result:
            if x == '1':
                str += '#'
            else:
                str += ' '
        answer.append(str)
    return answer

def solution2(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12 = a12.rjust(n,'0')
        a12 = a12.replace('1','#')
        a12 = a12.replace('0',' ')
        answer.append(a12)
    return answer