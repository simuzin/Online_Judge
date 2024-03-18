from collections import deque
def solution(A, B): 
    answer = -1
    deque_A, deque_B = deque(),deque()
    for i in range(len(A)):
        deque_A.append(A[i])
        deque_B.append(B[i])
    print(deque_A)
    for i in range(len(A)):
        if deque_A == deque_B:
            answer = i
            break
        deque_A.rotate(1)
    return answer