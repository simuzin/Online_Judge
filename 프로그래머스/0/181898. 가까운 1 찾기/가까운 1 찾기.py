def solution(arr, idx):
    answer = -1
    arr = arr[idx:]
    for i, n in enumerate(arr):
        if n == 1:
            answer = i + idx
            break
    return answer