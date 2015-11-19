# str - строки
empty_string = ''
name = 'Вася'
surname = "Пупкин"

full_name = name + surname

# name[0] = 'Б'  # Error: Неизменяемая
print("name[1] = ", name[1])  # Упорядоченная


# list - списки
empty_list = []
my_list = [1, 2, "Вася", (1, 4), [2, 4, 6]]

my_list[1] = 3  # Изменяемый
my_list.append('new')  # Добавление нового элемента
print("my_list = ", my_list)

print("my_list[4] = ", my_list[4])  # Упорядоченный
# print(my_list[6])  # Error: нельзя обращаться к несуществующему эдементу списка


# tuple - кортежи
my_tuple = (1, 2, "Вася", (1, 4), [2, 4, 6])

# my_tuple[2] = 'Нова строка'  # Error: Неизменяемый

print("my_tuple[2] = ", my_tuple[2])  # Упорядоченный


# dict - словарь
people = {'name': "Василий", 'middle_name': 'Васильевич',
          'surname': 'Чапаев', 'hobbies': ['лыжи', 'чтение']}

people['name'] = 'Петр'  # Изменяемый
people['age'] = 12  # Добавление нового элемента

# print("people[1] = ", people[1])  # Неупорядоченный
print("people[name] = ", people['name'])  # Обращение по ключу

# set
s = {2, 4, 5, 7, 7, 7}
print(s)
