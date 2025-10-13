import sys
input = sys.stdin.readline

N = int(input().strip())

flag = False
for i in range(1, 1000000):
    if N == i+sum(list(map(int, str(i)))):
        print(i)
        flag =True
        break
if flag == False:
    print("0")