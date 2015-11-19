# Обход последовательностей
# fruits = ['orange', 'apple', 'pea', 'kiwi']
# # Задача-1: Вывести элементы на экран последовательно
# # Плохое решение
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1  # i = i + 1
#
# # Хорошее решение (python style :-) )
# for fruit in fruits:
#     print(fruit)

people = {'name': "Василий", 'middle_name': 'Васильевич', 'surname': 'Чапаев', 'hobbies': ['лыжи', 'чтение']}
# # Задача-2: Сформировать и вывести список всех параметров(свойств) человека
# people_properties = []
# for key in people.keys():  # неявно
#     people_properties.append(key)
# print(people_properties)


# Задача-2.1 Вывести информацию о человеке
print("\n*****PEOPLE********")
for key, value in people.items():   # Множественное присваивание
    print("%s: %s" % (key, value))  # Форматирование строки

