def solution(str1, str2):
    temp, _str1 = [], []
    for s in str1.lower():
        temp.append(s)
        if len(temp) == 2:
            a = ''.join(temp)
            if a.isalpha():
                _str1.append(a)
            temp.pop(0)
    temp, _str2 = [], []
    for s in str2.lower():
        temp.append(s)
        if len(temp) == 2:
            a = ''.join(temp)
            if a.isalpha():
                _str2.append(a)
            temp.pop(0)
    cnt,len_1, len_2 = 0, len(_str1), len(_str2)
    for i in _str1:
        if i in _str2:
            cnt +=1
            _str2.pop(_str2.index(i))
    if (len_1+len_2-cnt) != 0:
        sim = cnt/(len_1+len_2-cnt) 
    else: sim = 1
    return int(sim * 65536)