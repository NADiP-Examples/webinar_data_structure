# Генераторы списков для обработки структур
peoples = [
    {
        'name': 'Иван',
        'surname': 'Иванов',
        'age': 19,
        'hobbies': ['лыжи', 'программирование']
    },
    {
        'name': 'Петр',
        'surname': 'Репкин',
        'age': 26,
        'hobbies': ['литература', 'рисование']
    },
    {
        'name': 'Алексей',
        'surname': 'Белый',
        'age': 18,
        'hobbies': ['лыжи', 'литература']
    },
    {
        'name': 'Федор',
        'surname': 'Достоевский',
        'age': 194,
        'hobbies': ['литература', 'философия']
    }
]

# Задача-1: Вывести список имен людей младше 20 лет
young_peoples = [people['name'] for people in peoples if people['age'] < 20]
print(young_peoples)

# Вывести средний возраст всех людей
average_year = sum([people['age'] for people in peoples])/len(peoples)
print(average_year)

# Вывести полные имена(Имя и Фамилия)всех людей с хобби 'литература'
hobby = 'литература'
peoples_with_hobby = ["%s %s " % (people['name'], people['surname'])
                      for people in peoples
                      if hobby in people['hobbies']]
print(peoples_with_hobby)
