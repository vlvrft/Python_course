# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

import os

os.system('CLS')

number = int(input("Введите номер билета: "))

n = len(str(number))
while n % 2 == 1 or n == 0:
    print("Вы ввели некорректное число")
    number = int(input("Повторите попытку: "))
    n = len(str(number))


number_right = str(number)[len(str(number))//2:]
number_left = str(number)[0:len(str(number))//2]
numStrIntL = int(number_left)
numStrIntR = int(number_right)

sumLeft = 0
sumRight = 0
while (numStrIntL != 0 or numStrIntR != 0):
    sumLeft = sumLeft + numStrIntL % 10
    numStrIntL = numStrIntL // 10
    sumRight = sumRight + numStrIntR % 10
    numStrIntR = numStrIntR // 10
if sumLeft == sumRight:
    print("Счастливый билетик")
else:
    print("Обычный билетик")


