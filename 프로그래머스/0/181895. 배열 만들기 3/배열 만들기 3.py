def solution(arr, intervals):
    answer = []
    for a,b in intervals:
        temp = arr[a:b+1]
        answer.extend(temp)
    return answer