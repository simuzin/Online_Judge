students = [i for i in range(1,31)]
for _ in range(28):
    students.pop(students.index(int(input())))

for i in students:
    print(i)