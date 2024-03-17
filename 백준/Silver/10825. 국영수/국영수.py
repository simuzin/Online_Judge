import sys
n = int(sys.stdin.readline().strip())
students = {}
for _ in range(n):
    name,korean,english,math = sys.stdin.readline().strip().split()
    students[name] = [int(korean), int(english), int(math)]
students_sorted = list(sorted(students.items(), key = lambda x:(-x[1][0],x[1][1],-x[1][2],x[0])))
for student in students_sorted:
    print(student[0])