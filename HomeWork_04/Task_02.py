# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

num = int(input("Введите число: "))
for i in range(1, num + 1):
    if(num % i == 0):
        print(i)