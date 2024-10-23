import numpy as np
def solution(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    arr3 = np.dot(arr1, arr2)
    answer = arr3.tolist()
    return answer