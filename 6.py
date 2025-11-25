import math
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
def calculate_triangle_area(a, b, c):
    a = side1
    b = side2
    c = side3
    p = (a+b+c)/2
    Geron = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return Geron
x1, y1, x2, y2 = map(float, input("Координаты А и В: ").split())
side1 = calculate_distance(x1, y1, x2, y2)
tochki2 = map(float, input("Координаты В и С: ").split())
side2 = calculate_distance(*tochki2)
tochki3 = map(float, input("Координаты С и А: ").split())
side3 = calculate_distance(*tochki3)
print(f"Длина сторон: AB-{side1:.2f}, BC-{side2:.2f}, CA-{side3:.2f}")
Geron = calculate_triangle_area(side1, side2, side3)
print(f"Площадь треугольника по формуле Герона: {Geron:.2f} ")