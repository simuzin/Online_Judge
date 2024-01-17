from itertools import combinations
key = []
for _ in range(9):
    key.append(int(input()))
for comb in combinations(key,7):
    if (sum(comb) == 100):
        res = list(comb)
res.sort()
for i in range(7):
    print(res[i])