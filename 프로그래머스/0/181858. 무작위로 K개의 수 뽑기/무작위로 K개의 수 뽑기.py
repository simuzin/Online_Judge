def solution(arr, k):
    answer = []
    flag = False
    for i,n in enumerate(arr):
        if len(answer) >= k:
            print(answer, k)
            flag = True
            break
        if n not in answer:
            answer.append(n)
            
    # 완성된 배열(answer)의 길이가 k보다 작을 경우,        
    if not flag:
        for i in range(k - len(answer)):
            answer.append(-1)
    return answer