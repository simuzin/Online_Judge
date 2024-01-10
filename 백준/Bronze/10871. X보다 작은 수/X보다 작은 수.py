_,x = map(int, input().split())
a = list(map(int, input().split()))
answer = []
for i in a:
    if i < x:
        answer.append(i)
for i in answer:
    print(i, end = ' ')