# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

set1 = {randint(1, 15) for x in range(int(input("Введите желаемое количество элементов: ")))}
set2 = {randint(1, 15) for x in range(int(input("Введите желаемое количество элементов: ")))}
print(set1, set2)
set3 = set1.intersection(set2)
print(sorted(set3))
