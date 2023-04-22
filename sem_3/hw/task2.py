# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X


from random import randint
import os

os.system('CLS')

N = int(input("Введите количество элементов: "))

while N < 1:
    print("Число не можеть быть меньше 1!")
    N = int(input("Введите количество элементов: "))

arr = [randint(1, 10) for x in range(0, N)]
print(*arr)


num = int(input("Введите число: "))
index = 0
delta = abs(num - arr[0])

for i in range(1, N):
    new_delta = abs(num - arr[i])
    if new_delta < delta:
       delta = new_delta
       index = i 

print("Cамый близкий по величине элемент к заданному числу {} является число {}".format(num, arr[index]))

