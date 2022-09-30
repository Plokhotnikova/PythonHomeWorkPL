# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def values(x):
    xyz = ["X", "Y", "Z"]
    array = []
    for i in range(x):
        array.append(input(f'Введите значение {xyz[i]}: '))
    return array


def predicate(x):
    leftside = not (x[0] or x[1] or x[2])
    rightside = not x[0] and not x[1] and not x[2]
    result = leftside == rightside
    return result


examination = values(3)

if predicate(examination) == True:
    print('Верно')
else:
    print('Не верно')