from collections import deque
import sys

su = int(sys.stdin.readline().strip())
for _ in range(su): 
    n,m = map(int, sys.stdin.readline().strip().split())
    key = list(map(int, sys.stdin.readline().strip().split()))
    index = [i for i in range(n)]
    temp = deque(key)
    temp_index = deque(index)
    flag = 0
    while True:
        if temp:
            big = max(temp)
            if big == temp[0]:
                flag += 1
                if temp_index[0] == m:
                    print(flag)
                    break
                temp.popleft()
                temp_index.popleft()
            else:
                temp.rotate(-1)
                temp_index.rotate(-1)
        else:
            break
