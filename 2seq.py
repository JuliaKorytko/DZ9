"""МОДУЛЬ 2"""

# Пользователь вводит любые цифры через запятую
# Сохранить цифры в список
# Получить новый список в котором будут только уникальные элементы исходного
# Вывести новый список на экран
# Порядок цифр в новом списке не важен

numbers = input("Введите любые цифры через запятую: ")
sepa_numbers = numbers.split(",")
result_count = []
for number in sepa_numbers:
    if sepa_numbers.count(number) == 1:
       result_count.append(number)
print(result_count)





