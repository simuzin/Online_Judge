a = int(input())
for i in range(a):
    r,s = input().split()
    answer = ''
    for i in s:
        answer += i * int(r)
    print(answer)