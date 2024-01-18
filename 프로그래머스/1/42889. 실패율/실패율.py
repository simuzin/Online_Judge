def solution(N, stages):
    temp, key = [0] * (N+2), {}
    for stage in stages:
        temp[stage] += 1
    total = len(stages)
    for i in range(1, N+1):
        if total > 0:
            rate = temp[i] / sum(temp[i:])
            total -= temp[i]
        else:
            rate = 0
        key[i] = rate
    key = sorted(key.items(), key = lambda x:-x[1])
    return [a for a,_ in key]