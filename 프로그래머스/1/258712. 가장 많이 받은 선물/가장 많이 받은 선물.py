def solution(friends, gifts):
    answer = 0
    num = len(friends)
    chart =[[0]*num for i in range(num)]
    for g in gifts:
        give, take = g.split()
        chart[friends.index(give)][friends.index(take)] += 1
    
    score = []
    for i in range(num):
        temp = 0
        for j in range(num):
            temp += chart[j][i]
        score.append(sum(chart[i]) - temp)
    
    key = []
    for k in range(num):
        cnt = 0
        for i in range(num):
            if chart[k][i] > chart[i][k]:
                cnt += 1
            elif chart[k][i] == chart[i][k]:
                if score[k] > score[i]:
                    cnt += 1
        key.append(cnt)
    return max(key)