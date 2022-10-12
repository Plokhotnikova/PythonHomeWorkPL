# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

digits = input("Введите последовательность цифр: ")
tp = tuple(digits)
ans_ls = [c for c in tp if tp.count(c) == 1]
ans_ls = list(map(int, ans_ls))
print(ans_ls)