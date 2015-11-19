import os
import json
import time


def timer(fn):
    """
    Декоратор timer - выводит время выполнения декорируемой функции
    """
    def wrapped(*args):
        start = time.clock()
        result = fn(*args)
        return 'Функция выполнялась %.6f мс, результат: %s' \
               % (time.clock() - start, result)

    return wrapped


@timer
def load_data(file_name):
    with open(os.path.join('data', file_name), encoding='UTF-8') as f:
        peoples_data = json.load(f)
    return 'кол-во объектов в файле %d' % len(peoples_data)


print(load_data('peoples_many.json'))

