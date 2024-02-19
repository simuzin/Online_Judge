from collections import Counter
def solution(X, Y):
    answer, temp ='', []
    x_dict = dict(Counter(X))
    y_dict = dict(Counter(Y))
    
    for num in x_dict:
        if num in y_dict:
            print(num)
            for _ in range(min(x_dict[num], y_dict[num])):
                temp.append(num)
    
    if temp:
        if sum(int(i) for i in temp) == 0:
            answer = "0"
        else:
            temp.sort(reverse = True)
            answer = ''.join(str(i) for i in temp)
    else:
        answer = "-1"
    return answer