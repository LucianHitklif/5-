import math
def calculate_rectangle_area(width,height):
    rectangle = width * height
    return rectangle
def calculate_circle_area(radius):
    cirle = math.pi * radius**2
    return cirle
width, height = map(float, input('Введите ширину и высоту прямоугольника через пробел: ').split())
rect = calculate_rectangle_area(width, height)
print(f'Площадь прямоугольника:{rect}')
radius = float(input('Введите радиус круга: '))
circle = calculate_circle_area(width)
print(f'Площадь круга: {circle}')