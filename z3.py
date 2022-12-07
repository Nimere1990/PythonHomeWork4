# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы 
# фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4

from statistics import mean

with open('students.txt', 'w', encoding='utf-8') as f:
    f.write('''Ангела Меркель 5
Энакин Скайуокер 5
Фредди Меркури 3
Александр Пушкин 4
''')


def students(score: int, file='students.txt'):
    with open(file, encoding='utf-8') as f1:
        result_dict = {line.rsplit(' ', 1)[0]: line.strip().rsplit(' ', 1)[1].split(',') for line in f1}
        with open(file, 'w', encoding='utf-8') as f2:
            for k, v in result_dict.items():
                if mean(list(map(int, v))) > score:
                    f2.write(f'{k.upper()} {",".join(v)}\n')
                else:
                    f2.write(f'{k} {",".join(v)}\n')


students(4)