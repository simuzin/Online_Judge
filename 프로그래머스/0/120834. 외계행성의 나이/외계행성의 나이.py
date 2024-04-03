def solution(age):
    answer = ''
    alpha = ['a','b','c','d','e','f','g','h','i','j']
    for i in range(3,-1,-1):
        key = age//(10**i)
        age %= (10**i)
        if not answer and (key==0):
            continue
        answer += alpha[key]   
    return answer