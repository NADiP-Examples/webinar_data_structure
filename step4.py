# Генераторы списков
# numbers_list = [-1, 2, 4, 10, 4, 5, 3, -2, 0]
# # Задача-1: Умножить все элементы списка на n
# n = 4
# # Решение в лоб
# new_list = []
# for el in numbers_list:
#     new_list.append(el*n)
# numbers_list = new_list
# print(new_list)
#
# # Более изящное решение с помощью генераторов
# numbers_list = [el*n for el in numbers_list]
# print(new_list)


# numbers_list = [-1, 2, 4, 10, 4, 5, 3, -2, 0]
# # Задача-2: Удалить из списка все элементы > n
# n = 3
#
# for el in numbers_list[:]:  # В чем ошибка?
#     if el > n:
#         numbers_list.remove(el)
# print(numbers_list)
#
# # Решение через генератор списков, от обратного
# numbers_list = [el for el in numbers_list if el <= n]
# print(numbers_list)


# Задача-3: Создать список из последовательных целых чисел от a до b(a<b),
#  с шагом step
# Решаем через генератор
a = 4
b = 20
step = 5

step_list = [el for el in range(a, b) if (el-a) % step == 0]
print("new_list =", step_list)

# Без генератора
step_list = []
el = a
while el <= b:
    step_list.append(el)
    el += step
print("new_list =", step_list)

