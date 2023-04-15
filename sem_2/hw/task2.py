# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))

num_1 = 1

while num_1 < p:
    num_2 = s - num_1
    if s == num_1 + num_2 and p == num_2 * num_1:
        print(num_1, num_2)
        break
    num_1 += 1

# -----варианты----

# from math import sqrt

# s = int(input())
# p = int(input())

# if s**2-4*p < 0:
# print("No real-valued solutions exist")
# else:
# y = int((s+sqrt(s**2-4*p))/2)
# print(s-y, y)




# import math

# summa = int(input("Введите сумму чисел: "))
# multiply = int(input("Введите произведение чисел: "))

# d = summa ** 2 - 4 * multiply

# if d >= 0:
# x1 = int((summa + math.sqrt(d)) / 2)
# x2 = int((summa - math.sqrt(d)) / 2)
# y1 = summa - x1
# y2 = summa - x2
# print(f"Результат №1 : [{x1}, {y1}]")
# print(f"Результат №2 : [{x2}, {y2}]")
# else:
# print("Дискриминант не может быть меньше 0!")