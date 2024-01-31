temp = []
for _ in range(5):
    n = int(input())
    if n >= 40:
        temp.append(n)
    else:
        temp.append(40)
print(int(sum(temp)/5))