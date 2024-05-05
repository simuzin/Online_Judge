def solution(num, k):
    answer = 0
    length = len(str(num))
    cnt = 0
    while num > 0:
        cnt += 1
        if num % 10 == k:
            answer = cnt
        num //= 10
    return (length - answer + 1) if answer else -1