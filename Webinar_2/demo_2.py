import os
import json
from pprint import pprint  # pprint - используем для красиво-отформатированного вывода

# Загружаем данные из файла json, и преобразуем в структуру python
with open(os.path.join('data', 'peoples.json'), encoding='UTF-8') as f:
    peoples_data = json.load(f)

# Задача: Получить список людей, чей возраст равен 19
# Решение:
pprint(list(filter(lambda p: p['age'] == 19, peoples_data)))

# Задача: Получить список имен людей
# Решение:
pprint(list(map(lambda p: p['name'], peoples_data)))
