# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 8]
# print(*list_1) # *убирает скобочки, раскрывает список

# print(len(list_1))
# print(list_1[3])

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# Основные действия со списками:
# 1. Удаление последнего элемента списка.
# Метод pop удаляет последний элемент из списка:
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop()) # 0
print(list_1) # [12, 7, -1, 21]
print(list_1.pop()) # 21
print(list_1) # [12, 7, -1]
print(list_1.pop()) # -1
print(list_1) # [12, 7]

# 2. Удаление конкретного элемента из списка.
# Надо указать значение индекса в качестве аргумента функции pop:
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0)) # 12
print(list_1) # [7, -1, 21, 0] 

# 3. Добавление элемента на нужную позицию.
#  Функция insert — указание индекса (позиции) и значения.
list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11))
print(list_1) # [12, 7, 11, -1, 21, 0]

# Срез списка
# Помните в конце первой лекции Вы прошли срезы строк? Также существует срез списка,
# давайте научимся изменять наш список
# ● Отрицательное число в индексе — счёт с конца списка
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0]) # 1
print(list_1[1]) # 2
print(list_1[len(list_1)-1]) # 10
print(list_1[-5]) # 6
print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2]) # [1, 2]
print(list_1[len(list_1)-2:]) #[9, 10]
print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18]) # []
print(list_1[0:len(list_1):6]) # [1, 7]
print(list_1[::6]) # [1, 7]

