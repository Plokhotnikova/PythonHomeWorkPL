# Реализуйте алгоритм перемешивания списка
import random
random_list = [random.randint(0,100) for i in range(5)]
print(random_list)  # cоздали и вывели на экран случайный список

random.shuffle(random_list)
print(random_list)  # перемешали созданный список