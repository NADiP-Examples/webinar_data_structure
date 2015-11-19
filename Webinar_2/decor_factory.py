# Фабрика декораторов - умножает результат декорируемой функции на n, если умножение невозможно возвращает None
def multiple(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            try:
                return res * n
            except TypeError:
                return None

        return wrapper

    return decorator


# Примеры использования фабрики декораторов

# Текст можно умножать на целое число
@multiple(2)
def hello(text):
    return text


@multiple(4.2)
def func_1(x, y):
    return x + y


# Результ (словарь) нельзя умножать --> декоратор возвращает None
@multiple(2)
def func_2(a, b):
    return {'a': a, 'b': b}


print(func_1(2, 3))
print(func_2(2, 3))
print(hello('Hi, User -)'))
