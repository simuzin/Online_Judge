result = []
for i in range(1, 9980):
    num_to_list = list(map(int, str(i)))
    result.append(i + sum(num_to_list))

result.sort()
for i in range(1, 10000+1):
    if i not in result:
        print(i)