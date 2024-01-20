n = int(input())
f = int(input())
n = n // 100 * 100
for i in range(100):
    if (n + i) % f == 0:
        if i // 10 == 0:
            print(f'0{i}')
        else:
            print(i)
        break
