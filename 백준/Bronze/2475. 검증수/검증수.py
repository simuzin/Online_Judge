temp = list(map(int, input().split()))
answer = 0
for i in temp:
    answer += i**2
print(answer % 10)