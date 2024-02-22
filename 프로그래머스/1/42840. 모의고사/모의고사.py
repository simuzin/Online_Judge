def solution(answers):
    answer = []
    cnt = [0,0,0]
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == a[i%5]:
            cnt[0] += 1
        if answers[i] == b[i%8]:
            cnt[1] += 1
        if answers[i] == c[i%10]:
            cnt[2] += 1
            
    m  = max(cnt)
    if cnt[0] == m:
        answer.append(1)
    if cnt[1] == m:
        answer.append(2)
    if cnt[2] == m:
        answer.append(3)
    
    return answer