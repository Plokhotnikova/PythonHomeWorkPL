# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random
random_list = [random.randint(0,100) for i in range(5)]
print(random_list)  # cоздали и вывели на экран случайный список

sum = 0
for i in range(1, len(random_list)):
    if i % 2 != 0:
        sum += random_list[i]
print(sum)