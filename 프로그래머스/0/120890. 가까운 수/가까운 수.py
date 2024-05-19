def solution(array, n):
    answer = []
    temp = [abs(i-n) for i in array]
    
    for i,n in enumerate(temp):
        if n == min(temp):
            answer.append(array[i])
    return min(answer)