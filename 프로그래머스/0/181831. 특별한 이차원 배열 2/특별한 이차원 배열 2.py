def solution(arr):
    answer = 1
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == arr[j][i]:
                continue
            else:
                answer = 0
                break
    return answer