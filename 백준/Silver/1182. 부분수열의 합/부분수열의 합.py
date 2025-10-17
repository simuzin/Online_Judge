import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

# (부분)수열 구하는 함수
def perm(start, depth, stop):
    if depth == stop:
        perm_result.append(temp.copy())
        return
    for i in range(start, N):
        if visited[i] == False:
            visited[i] = True
            temp.append(nums[i])
            perm(i+1, depth+1, stop)
            temp.pop()
            visited[i] = False

# 부분순열의 합 & S값과 비교
for i in range(1, N+1):
    temp = []
    perm_result = []
    visited = [False] * N
    perm(0,0,i)
    # print(perm_result)
    for j in range(len(perm_result)):
        if S == sum(perm_result[j]):
            cnt += 1

print(cnt)