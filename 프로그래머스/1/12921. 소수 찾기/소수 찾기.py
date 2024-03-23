def solution(n):
    temp = [False, False] + [True] * (n -1)
    prime = []
    
    for i in range(2, n+1):
        if temp[i]:
            prime.append(i)
        for j in range(2*i,n+1,i):
            temp[j] = False
    return len(prime)