def draw_point(coords):
    print('point: (%s %s)' % coords)

x = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8]
y = [-24, -20, -16, -12, -8, -4, 0, 4, 8, 12]

# Задача: передать координаты функции draw_point в виде пар координат (x, y)

# Решение-1: for in + zip
# for point in zip(x, y):
#     draw_point(point)

# Решение-2
# list(map(draw_point, zip(x, y)))

# Решение-3: через генератор списков + zip
[draw_point(point) for point in zip(x, y)]
