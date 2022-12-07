# 1 - Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

num = int(input('Введите число N: \n'))
firstnum = num
lst = []
i = 2 
while i <= num:
        if num % i == 0:
                lst.append(i) 
                num //= i
        else:
                i += 1
if num > 1:
        lst.append(num)
b = set(lst)
print(f'Список простых множителей для числа {firstnum}:\n{b}')