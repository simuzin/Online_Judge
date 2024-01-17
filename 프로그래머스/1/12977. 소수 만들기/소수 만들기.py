from itertools import combinations
def solution(nums):
    answer = 0
    combs = combinations(nums,3)
    for comb in combs:
        key, flag = sum(comb), 0
        for i in range(2, key):
            if key % i == 0:
                flag += 1
                break
        if flag == 0:
            answer += 1
    return answer