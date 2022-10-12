# Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

from math import *

eps = input("Введите точность вычисление: ")
#Нужно найти округление
s = eps
s = s.split('.')
cnt = len(s[1])
eps = float(eps)
i = 0
Phi = 0.0
while fabs(pow(-1.0, i) / (2 * i + 1)) >= eps:
    Phi += (pow(-1.0,i) / (2 * i + 1.0))
    i += 1.0
Phi *= 4.0
Phi = round(Phi, cnt)
print(Phi)
