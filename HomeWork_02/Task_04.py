# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

file_name = 'text.txt'

import random
num = int(input('Введите число: '))
great_list = []
for _ in range(num):
    great_list.append(random.randint(-num, num))
print(great_list)

new_list = []

with open('text.txt', 'r') as data:
    new_list = data.red().split("\n")
    
multi = great_list[int(new_list(1))] * great_list[int(new_list[2])]
print(f'Произведение элементов на позициях {new_list[1]} и {new_list[2]} равно {multi}') 
