from collections import Counter
def solution(k, tangerine):
    answer = 0
    tangerine_cnt = dict(Counter(tangerine))
    key = dict(sorted(tangerine_cnt.items(), key=lambda x : -x[1]))
    for t in key:
        if k <= 0: break
        k -= key[t]
        answer += 1
    return answer