def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = ''
        key1 = bin(arr1[i])[2:].zfill(n)
        key2 = bin(arr2[i])[2:].zfill(n)
        for j in range(n):
            if key1[j] == '1' or key2[j] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)        
    return answer