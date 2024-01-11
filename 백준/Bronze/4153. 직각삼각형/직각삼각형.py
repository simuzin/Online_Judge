import math
import sys
while True:
    temp = list(map(int,sys.stdin.readline().strip().split()))
    if sum(temp) == 0:
        break
    temp.sort()
    if temp[2] == math.sqrt(temp[0]**2 + temp[1]**2):
        print("right")
    else:
        print("wrong")