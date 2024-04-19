def solution(arr):
    answer = 0
    while True:
        temp = 0
        for i, a in enumerate(arr):
            if (a >= 50) and (a % 2 == 0):
                arr[i] = a/2
                temp += 1
            elif (a < 50) and (a % 2 == 1):
                arr[i] = a*2+1
                temp += 1
        if temp == 0:
            break
        answer += 1
    return answer