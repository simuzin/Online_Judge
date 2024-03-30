def solution(my_string, indices):
    answer = ''
    indices.sort()
    print(indices)
    for i, c in enumerate(my_string):
        if not indices:
            answer += my_string[i:]
            break
        if i == indices[0]:
            indices.pop(0)
            continue
        answer += c
    return answer