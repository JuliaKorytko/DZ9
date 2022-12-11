"""МОДУЛЬ 3"""

# Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
# Затем он вводит элементы 2-го списка
# Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран

amount_of_elements = int(input("Введите количество элементов для первого списка: "))

first_result = []

for i in range(amount_of_elements):
    numbers = int(input("Введите число в первый список: "))
    first_result.append(numbers)

print(first_result)

amount_of_elements = int(input("Введите количество элементов для второго списка: "))
second_result = []
for i in range(amount_of_elements):
    numbers = int(input("Введите число во второй список: "))
    second_result.append(numbers)
print(second_result)

print(set(first_result) - set(second_result))



