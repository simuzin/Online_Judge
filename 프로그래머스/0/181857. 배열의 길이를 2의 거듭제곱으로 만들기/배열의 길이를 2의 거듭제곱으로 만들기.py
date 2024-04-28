def solution(arr):
    answer = []
    key = [1,2,4,8,16,32,64,128,256,512,1024]
    for i in key:
        if len(arr) > i:
            continue
        else:
            answer = arr
            for j in range(i-len(arr)):
                answer.append(0)
            break
    return answer