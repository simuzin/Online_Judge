from collections import Counter

def solution(arr):
    answer = []
    if 2 in arr:
        arr_cnt = Counter(arr)
        if arr_cnt[2] > 1:
            a = arr.index(2)
            arr_inv = arr[::-1]
            b = len(arr_inv) - arr_inv.index(2)
            answer = arr[a:b]
        else:
            answer.append(2)
    else:
        answer.append(-1)
    return answer