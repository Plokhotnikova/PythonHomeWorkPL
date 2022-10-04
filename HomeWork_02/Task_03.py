# Задайте список из n чисел последовательности (1+1/n)^n
# и выведите на экран их сумму.

def Subsequence(num):
    list = []
    for i in range(1, num + 1):
        list.append((1 + 1 / i) ** i)
    return list


def total(list):
    sum = 0
    for i in range (len(list)):
        sum += list[i]
    return sum
    
number = int(input('Введите число: '))

list = Subsequence(number)
print (f'Список чисел: {list}')
sum = total(list)
print ('Cумма чисел в списке: ', sum)
