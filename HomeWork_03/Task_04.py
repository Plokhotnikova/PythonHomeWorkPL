# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# минимальное значение дробной части отличное от нуля,
# у целых чисел дробной части нет их в расчет не берем
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random
random_list = [random.randint(0,100) + random.randint(0, 100) / 100 for i in range(5)]
print(random_list) 

newList = []
for i in range(len(random_list)):
    if random_list[i] % 1 != 0:
        newList.append(random_list[i] % 1)
print(max(newList) - min(newList))  