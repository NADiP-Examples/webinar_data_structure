alphabet = "абвгде"
letters_list = list(alphabet)  # список из строки
letters_tuple = tuple(alphabet)  # кортеж из строки
print("letters_list = ", letters_list)
print("letters_tuple = ", letters_tuple)
print(str(letters_list))  # а так не работает
print('/'.join(letters_list))


my_dict = dict((('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')))
print("my_dict = ", my_dict)


fruits = ['orange', 'apple', 'pea', 'orange', 'apple', 'apple']
unique_fruits = list(set(fruits))
print("---", unique_fruits)


people = {'name': "Василий", 'middle_name': 'Васильевич', 'surname': 'Чапаев', 'hobbies': ['лыжи', 'чтение']}
print(list(people.keys()))
print(people.values())
