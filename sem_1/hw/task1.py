# Задача 2: Найдите сумму цифр трехзначного числа.
import os

os.system('CLS')

number = int(input("Enter a number -> "))

n1 = number % 10
n2 = number % 100 // 10
n3 = number // 100
sumNumber = n1 + n2 + n3
print("Дано число {}, сумма элементов числа = {}".format(number, sumNumber))
