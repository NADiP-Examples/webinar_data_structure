# Создаем первый декоратор
def add_stars(fn):
    def wrapped(*args):
        print("*" * 10)
        fn(*args)
        print("*" * 10)

    return wrapped


# Создаем второй декоратор
def add_lines(fn):
    def wrapped():
        print("-" * 10)
        fn()
        print("-" * 10)

    return wrapped


@add_stars
def hello():
    print("Hello world")


@add_stars
@add_lines
def say_hello():
    print("Hello")


@add_stars
def print_text(text):
    print(text)


# Вызываем декорированную функцию
say_hello()


print_text('Simple text')
# Без декоратора можно было вызвать так: add_stars(print_text)()
