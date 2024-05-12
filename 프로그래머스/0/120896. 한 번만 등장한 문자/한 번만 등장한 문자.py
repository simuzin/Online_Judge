from collections import Counter
def solution(s):
    answer = []
    s_cnt = Counter(s)
    for i in set(s):
        if s_cnt[i] == 1:
            answer.append(i)
    answer.sort()
    return ''.join(answer)