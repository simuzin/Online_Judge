def solution(data, ext, val_ext, sort_by):
    key = {"code":0, "date":1, "maximum":2, "remain":3}
    temp = sorted(data, key = lambda x:x[key[ext]])
    for i in range(len(data)):
        if temp[len(data) - i - 1][key[ext]] >= val_ext:
            temp.pop(len(data) - i - 1)
        else:
            break
    temp = sorted(temp, key = lambda x:x[key[sort_by]])
    return temp