def solution(word):
    answer = 0
    alpha = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    
    for i, char in enumerate(word):
        value  = alpha[char]
        for j in range(5 - i):
            answer += (value  * (5 ** j))
        answer += 1     
    return answer