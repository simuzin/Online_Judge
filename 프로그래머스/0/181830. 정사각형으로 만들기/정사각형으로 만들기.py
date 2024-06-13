def solution(arr):
    r = len(arr)
    l = len(arr[0])
    if r > l :
        for i in range(r):
            temp = [0] * (r-l)
            arr[i].extend(temp)
    else:
          for i in range(l-r):
                temp = [0] * l
                arr.append(temp)
    return arr