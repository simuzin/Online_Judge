a,b,v = map(int, input().split())
key = v-a
daily_up = a-b

res = (key // daily_up) +1
if key % daily_up != 0:
    res += 1
print(res)