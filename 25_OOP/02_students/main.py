class Student:
    def __init__(self, full_name, number_g, academ_perfom):
        self.full_name = full_name
        self.number_g = number_g
        self.academ_perfom = academ_perfom

    def average_score(self):
        return sum(self.academ_perfom) / len(self.academ_perfom)

    def __str__(self):
        result = f'{self.full_name} {self.number_g} {self.average_score()}'
        return result


students = []

for i in range(2):
    print(f'Студент {i + 1}: ')
    full_name = input('имя: ')
    group_n = int(input('номер группы: '))
    academic_p = list(map(int, input("оценки: ").split()))
    students.append(Student(full_name, group_n, academic_p))

sort = sorted(students, key=lambda student: student.average_score())
print(*sort, sep='\n')