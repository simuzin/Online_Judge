from collections import Counter
def solution(strArr):
    temp = []
    for i in strArr:
        temp.append(len(i))
    many = Counter(temp).most_common(1)
    return many[0][1]