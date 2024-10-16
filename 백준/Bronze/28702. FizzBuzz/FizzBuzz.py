import sys

for i in range(1, 4):
    num = sys.stdin.readline().strip()
    if num.isdigit():
        hint_num, cnt = int(num), i

fizzbuzz = hint_num + (4 - cnt)
if fizzbuzz % 3 == 0:
    if fizzbuzz % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
else:
    if fizzbuzz % 5 == 0:
        print("Buzz")
    else:
        print(fizzbuzz)