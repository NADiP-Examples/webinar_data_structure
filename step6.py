# Сохраняем данные в файле
import os
import json

with open(os.path.join('data', 'peoples.json'), encoding='UTF-8') as f:
    peoples_data = json.load(f)


print(type(peoples_data))
