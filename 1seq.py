"""МОДУЛЬ 1"""

# Задание:Пользователь вводит количество элементов будущего списка.
# После этого по очереди по одной вводит любые цифры.
# Сохранить цифры в список. Отсортировать список по возрастанию и вывести на экран

amount_of_elements = int(input("Введите количество элементов: "))

result = []

for i in range(amount_of_elements):
    numbers = int(input("Введите число: "))
    result.append(numbers)
result.sort()
print(result)


