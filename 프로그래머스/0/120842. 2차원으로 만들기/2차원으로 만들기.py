def solution(num_list, n):
    answer = []
    for i,num in enumerate(num_list):
        if i % n == 0:
            answer.append([])
        answer[-1].append(num)
    return answer