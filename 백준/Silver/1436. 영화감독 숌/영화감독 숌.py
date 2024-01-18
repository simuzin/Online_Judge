n = int(input())
number, count = 666, 0
while True:
    if '666' in str(number):
        count += 1
    if count == n:
        print(number)
        break
    number += 1